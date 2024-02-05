import random
import matplotlib.pyplot as plt
import pandas as pd
import pyarrow, tabulate


def monte_carlo_simulation(num_experiments, num_cubes):
    """Виконує серію експериментів методом Монте-Карло."""

    random.seed(42)
    # Генерація експериментів
    experiments = [(random.randint(1, 6) for _ in range(num_cubes)) for _ in range(num_experiments)]
    res = {i: 0 for i in range(1 * num_cubes, 6 * num_cubes + 1)}
    for e in experiments:
        res[sum(e)] += 1

    return res


def format_results(results):
    """Форматування результатів експериментів."""
    total_count = sum(results.values())
    header = f"| Сума | Імовірність |\n|-------|------------|\n"
    return header + "\n".join(f"| {k} | {v * 100 / total_count:.2f}% ({v}/{total_count}) |" for k, v in results.items())


def generate_chart_with_multiple_lines():
    """Генерація графіка з множинними лініями."""
    exp = [10, 100, 1000, 10000, 100000, 1000000, 10000000]
    num_cubes = 2

    plt.plot([i for i in range(1 * num_cubes, 6 * num_cubes + 1)],
             [2.78, 5.56, 8.33, 11.11, 13.89, 16.67, 13.89, 11.11, 8.33, 5.56, 2.78], label=f'Analytical baseline')

    for n in exp:
        results = monte_carlo_simulation(n, num_cubes)
        total_count = sum(results.values())
        plt.plot(list(results.keys()), [k * 100 / total_count for k in results.values()], label=f'{n} runs')

    plt.xlabel('N бросків кубів')
    plt.ylabel('%')
    plt.title('Модель Монте-Карло для кубів з різною кількістю кидків кубів')
    plt.legend()

    plt.show()


if __name__ == "__main__":
    num_experiments = 10000000
    num_cubes = 2

    res = {'Сума': [x for x in range(1 * num_cubes, 6 * num_cubes + 1)]
        , 'Аналітична імовірність, %': [2.78, 5.56, 8.33, 11.11, 13.89, 16.67, 13.89, 11.11, 8.33, 5.56, 2.78]
           }

    results = monte_carlo_simulation(num_experiments, num_cubes)
    res['Монте-Карло 10М, %'] = [v * 100 / num_experiments for v in results.values()]
    print(format_results(results))
    print('\n\n')

    num_experiments = 100000
    num_cubes = 2

    results = monte_carlo_simulation(num_experiments, num_cubes)
    res['Монте-Карло 100k, %'] = [v * 100 / num_experiments for v in results.values()]
    print(format_results(results))
    print('\n\n')

    df = pd.DataFrame(res)
    df['Різниця 10М, %'] = df['Монте-Карло 10М, %'] - df['Аналітична імовірність, %']
    df['Різниця 100k, %'] = df['Монте-Карло 100k, %'] - df['Аналітична імовірність, %']

    df['Аналітична імовірність'] = ['2.78% (1/36)',
                                    '5.56% (2/36)',
                                    '8.33% (3/36)',
                                    '11.11% (4/36)',
                                    '13.89% (5/36)',
                                    '16.67% (6/36)',
                                    '13.89% (5/36)',
                                    '11.11% (4/36)',
                                    '8.33% (3/36)',
                                    '5.56% (2/36)',
                                    '2.78% (1/36)']

    df['Монте-Карло 10М'] = df['Монте-Карло 10М, %'].apply(lambda x: f'{x:.2f}% ({x / 100 * 10000000:.0f}/10000000)')
    df['Монте-Карло 100k'] = df['Монте-Карло 100k, %'].apply(lambda x: f'{x:.2f}% ({x / 100 * 100000:.0f}/100000)')

    print(df[['Сума', 'Аналітична імовірність', 'Монте-Карло 100k',
              'Різниця 100k, %', 'Монте-Карло 10М', 'Різниця 10М, %']].to_markdown(index=False))

    generate_chart_with_multiple_lines()
