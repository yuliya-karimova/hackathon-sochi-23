import pandas as pd
from tqdm import tqdm
import shap
import catboost 
import math
from catboost import CatBoostRegressor, Pool
from sklearn.model_selection import train_test_split

result_df = pd.read_excel('C:\\Users\\Денис\\Desktop\\python\\hackathon3\\7.xlsx')

result_df = result_df.dropna(subset=['life_expectancy'])

# Определим признаки и целевую переменную
X = result_df.drop(['Unnamed: 0', 'id', 'region_id', 'name', 'longitude', 'latitude', 'region_name', 'group_name',
                    'house_points', 'street_points',
       'park_points', 'business_points', 'social_points', 'common_points',
       'total_points',
       'people_count', 'group_id', 'emblem_url', 'cardio_resp_mortality', 'life_expectancy', 'athlete',
       'athlete_children', 'mental_disorders', 'self_assessment '], axis=1)
y = result_df['life_expectancy']

# Разделим данные на тренировочную и тестовую выборку
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Определите, какие из ваших признаков являются категориальными
categorical_features = ['climate','park_group']  

# Создаем пулы данных для CatBoost
train_pool = Pool(X_train, y_train, cat_features=categorical_features)
test_pool = Pool(X_test, y_test, cat_features=categorical_features)

# Инициализируем и обучаем модель
model = CatBoostRegressor(
    iterations=1000,
    learning_rate=0.1,
    depth=6,
    cat_features=categorical_features,
    verbose=200
)
model.fit(train_pool, eval_set=test_pool)

# Оценим качество модели на тестовых данных
preds = model.predict(test_pool)
mse = ((preds - y_test) ** 2).mean()
print(f"Mean Squared Error: {mse}")

# Если нужно, можно сохранить обученную модель:
# model.save_model("catboost_model.cbm")

explainer = shap.Explainer(model)

# Вычислиv значения SHAP для набора данных
shap_values = explainer(X)
shap.summary_plot(shap_values, X, plot_type="bar")

# Используем TreeExplainer для объяснения предсказаний модели
tree_explainer = shap.TreeExplainer(model)
shap_values = tree_explainer.shap_values(X)

# Визуализируем значимость признаков для всего набора данных
shap.summary_plot(shap_values, X)
tree_explainer = shap.TreeExplainer(model)
shap_values = tree_explainer.shap_values(X)
base_values = tree_explainer.expected_value

shap.initjs()

# Перебор каждой строки и сохранение force_plot
for i in range(1,65):
    shap.force_plot(
        base_value=base_values,
        shap_values=shap_values[i],
        features=X.iloc[i],
        show=False,
        matplotlib=True
    )
    filepath = f"shap/{i+100}.html"
    shap.save_html(filepath, shap.force_plot(base_value=base_values, shap_values=shap_values[i], features=X.iloc[i], show=False))

