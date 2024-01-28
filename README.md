# Висновки:
- Task 1
    здійснено аналіз заданого графа, а саме визначено кількість вершин та ребер, чи відноситься граф до звязаного, густину графа, ступені вершин, ступені центральності, близкість вузла до іншиз вузлів та посередництво вузла. Виконавши повний аналіх заданого графа стає зрозуміло, які саме вузли мають найбільші значення відповідних характеристик, та можливість комплексного аналізу цілої картини. Це дозволяє краще зрозуміти алгоритми пошуку, які розглядаються в наступних завданнях.
- Task 2
    в даній задачі було розроблено два алгоритми пошуку, а саме: пошук в глибину (DFS) та пошук в ширину (BFS). Отримані результати дозволяють сказати, про суттєву відмінність в результатах обох алгоритмів. Так як для алгоритму DFS є характерним, пошук від кореневого вузла і вниз до листків, а для BFS - ступеневий пошук по  всім вузлам-нащадкам, а далі по їх нащадкам, то для знаходження найкоротшого маршруту найкраще підходить алгорит BFS.
Task 3
    виходячи з висновку попередньої задачі, найдоцільнішим алгоритмом пошуку для знаходження найкоротшого шляху є алгоритм BFS. Тому не дивно, що алгоритм Дейкстри є подібним до нього. В даному завданні було додано ваги ребрам графа заданого в Task 1. Використовуючи алгоритм Дейкстри було знайдено всі можливі найкоротші шляхи від всіх заданих вершин до усіх інших вершин. Даний приклад дозволяє, хоча б трохи, зрозуміти принципи роботи таких програм як навігатори.