import time
import tracemalloc
import random
import multiprocessing as mp
import pandas as pd
import matplotlib.pyplot as plt
import ace_tools_open as tools  # Used for displaying tables

from skip_list import SkipList  # Assuming SkipList is implemented in skip_list.py

class SkipListBenchmark:
    def __init__(self, plot_results=False):
        """
        Initialize the benchmarking class.
        :param plot_results: Boolean flag to determine if results should be plotted.
        """
        self.plot_results = plot_results

    def measure_time_memory(self, func, *args):
        """
        Measures execution time and memory usage of a function.
        :param func: Function to measure.
        :param args: Arguments for the function.
        :return: Tuple (execution time, memory usage).
        """
        tracemalloc.start()
        start_time = time.time()
        func(*args)
        end_time = time.time()
        memory_used = tracemalloc.get_traced_memory()[1] / 1024  # Convert to KB
        tracemalloc.stop()
        return (end_time - start_time, memory_used)

    def benchmark_operations(self, num_elements):
        """
        Benchmarks insert, search, and delete operations for a given number of elements.
        :param num_elements: Number of elements to test.
        :return: Dictionary with metrics.
        """
        skip_list = SkipList()
        elements = random.sample(range(1, num_elements * 10), num_elements)

        # Measure insert operation
        insert_time, insert_memory = self.measure_time_memory(self.insert_elements, skip_list, elements)

        # Measure search operation
        search_elements = random.sample(elements, min(100, len(elements)))  # Search 100 random elements or all if less
        search_time, search_memory = self.measure_time_memory(self.search_elements, skip_list, search_elements)

        # Measure delete operation
        delete_time, delete_memory = self.measure_time_memory(self.delete_elements, skip_list, search_elements)

        return {
            "Elements": num_elements,
            "Insert Time (s)": round(insert_time, 6),
            "Insert Memory (KB)": round(insert_memory, 2),
            "Search Time (s)": round(search_time, 6),
            "Search Memory (KB)": round(search_memory, 2),
            "Delete Time (s)": round(delete_time, 6),
            "Delete Memory (KB)": round(delete_memory, 2),
        }

    def insert_elements(self, skip_list, elements):
        """ Inserts elements into the skip list. """
        for elem in elements:
            skip_list.insert(elem)

    def search_elements(self, skip_list, elements):
        """ Searches for elements in the skip list. """
        for elem in elements:
            skip_list.search(elem)

    def delete_elements(self, skip_list, elements):
        """ Deletes elements from the skip list. """
        for elem in elements:
            skip_list.delete(elem)

    def run_benchmark(self, start, end, steps=10):
        """
        Runs the benchmark in parallel for a range of input sizes.
        :param start: Starting number of elements.
        :param end: Ending number of elements.
        :param steps: Number of groups to benchmark.
        """
        step_size = (end - start) // (steps - 1)
        element_sizes = [start + i * step_size for i in range(steps)]

        print(f"Running benchmarks in parallel on {mp.cpu_count()} CPU cores...")

        # Use multiprocessing to speed up execution
        with mp.Pool(processes=mp.cpu_count()) as pool:
            results = pool.map(self.benchmark_operations, element_sizes)

        # Convert results to a DataFrame
        df = pd.DataFrame(results)
        tools.display_dataframe_to_user(name="Skip List Benchmark", dataframe=df)

        # Plot results if required
        if self.plot_results:
            self.plot_results_graph(df)

    def plot_results_graph(self, df):
        """Plots benchmark results with interactive legend selection."""
        plt.figure(figsize=(12, 6))

        def plot_subplot(index, y_metrics, title, ylabel):
            """Helper function to plot a single subplot."""
            ax = plt.subplot(1, 2, index)
            lines = []
            for metric in y_metrics:
                line, = ax.plot(df["Elements"], df[metric], marker="o", label=metric, picker=True)
                lines.append(line)

            ax.set_xlabel("Number of Elements")
            ax.set_ylabel(ylabel)
            ax.set_title(title)
            ax.legend(loc="upper left", fontsize="small", frameon=True)

            # Make legend interactive
            def on_pick(event):
                legend = ax.legend_  # Get current legend
                for legline, origline in zip(legend.get_lines(), lines):
                    if legline == event.artist:
                        visible = not origline.get_visible()
                        origline.set_visible(visible)
                        legline.set_alpha(1.0 if visible else 0.2)  # Dim legend text if hidden
                        plt.draw()

            plt.gcf().canvas.mpl_connect("pick_event", on_pick)

        # Plot operation times
        plot_subplot(1, ["Insert Time (s)", "Search Time (s)", "Delete Time (s)"], 
                    "Skip List Operation Times", "Time (s)")

        # Plot memory usage
        plot_subplot(2, ["Insert Memory (KB)", "Search Memory (KB)", "Delete Memory (KB)"], 
                    "Skip List Memory Usage", "Memory Usage (KB)")

        plt.show()


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Benchmark Skip List Performance")
    parser.add_argument("start", type=int, help="Number of elements to insert (or start range)")
    parser.add_argument("--end", type=int, help="End range for testing multiple inputs")
    parser.add_argument("--steps", type=int, default=10, help="Number of steps in range testing")
    parser.add_argument("--plot", action="store_true", help="Plot results instead of just displaying them")

    args = parser.parse_args()
    benchmark = SkipListBenchmark(plot_results=args.plot)

    if args.end:
        benchmark.run_benchmark(args.start, args.end, args.steps)
    else:
        benchmark.run_benchmark(args.start)
