# hackathon-sochi-23

🚀🌆 AI Sister на страже вашего здоровья! 🌆🚀
🌍 Более 100 городов России. 📊 150+ признаков инфраструктуры. 🔬 Глубокий статистический анализ. 🚀 Технологии градиентного бустинга для моделирования (ИИ)🌿 Основные факторы здоровья горожан под нашим микроскопом.
Команда "AI Sister" провела комплексный исследовательский проект, целью которого является анализ городской инфраструктуры и её влияния на здоровье населения. Произведен детальный статистический анализ, позволяющий выделить ключевые факторы, влияющие на здоровье горожан. Для прогнозирования показателей здоровья была разработана модель на основе алгоритма градиентного бустинга catboost.
Разработано веб-приложение для визуализации результатов анализа. В приложении представлена интерактивная карта, на которой отображаются объекты городской инфраструктуры, а также их влияние на здоровье населения.
На основании проведенного исследования можно предоставить рекомендации для органов местного самоуправления по улучшению городской среды.
Frontend – Содержит материалы, разметку, шаблоны для отображения сайта.
В папке docs – находится научный отчет по предикторам
Backend:
App.py – запускает веб приложение
added.py – Данный скрипт необходим для сбора дополнительных признаков и их сохранения.
map.py – Данный скрипт отрисовывать карту. Отмечает полигон города полигоны парков и ставят зеленые, красные и голубые метки.
model.py – Данный скрипт обучает модель CatBoost. И рисуют графики, которые оценивают при дикторы.
park.py – Данный скрипт считает количество негативных точек возле парков.
plot.py – Данные скрипты отрисовывать графики для анализа.
school.py – Данный скрипт считает количество негативных точек возле школ и других учебных заведений.
text.py – Данный скрипт составляет текстовое описание в зависимости от проблем в городе и дает рекомендации
1.ipynb – Рабочая тетрадь со всем решением. Содержит все промежуточные варианты анализа
