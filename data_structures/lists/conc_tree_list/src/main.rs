use clap::Parser;
use conc_tree_list::ConcTreeList; // Ensure your lib.rs exports ConcTreeList
use rand::prelude::*;
use std::time::Instant;

// Import the color types and constants from plotters.
use plotters::prelude::RGBColor;
use plotters::prelude::full_palette::{RED, BLUE, GREEN, CYAN, AMBER};

/// Command-line arguments for the benchmark.
#[derive(Parser, Debug)]
#[command(author, version, about, long_about = None)]
struct Args {
    /// Starting number of elements for the benchmark.
    start: usize,
    /// Ending number of elements to test (if omitted, a single benchmark with "start" elements is run).
    #[arg(long)]
    end: Option<usize>,
    /// Number of steps in the range (default is 10).
    #[arg(long, default_value_t = 10)]
    steps: usize,
    /// If set, generate a combined graph image ("benchmark_combined.png").
    #[arg(long)]
    plot: bool,
    /// If set, print the results as a table in the console.
    #[arg(long)]
    table: bool,
}

/// Structure to store the benchmark results for a given input size.
struct BenchmarkResult {
    elements: usize,
    build_time: f64,
    search_time: f64,
    delete_at_time: f64,
    insert_at_time: f64,
    append_time: f64,
}

/// Measures the execution time of a closure.
fn measure_time<F: FnOnce()>(f: F) -> f64 {
    let start = Instant::now();
    f();
    start.elapsed().as_secs_f64()
}

/// Benchmarks several operations on a ConcTreeList:
/// - Build (using from_vec)
/// - Search (using get)
/// - Delete_at (using delete_at)
/// - Insert_at (using insert_at)
/// - Append (using concat)
fn benchmark_operations(num_elements: usize) -> BenchmarkResult {
    let mut rng = rand::thread_rng();

    // Generate a vector of random numbers.
    let elements: Vec<i32> = (0..num_elements)
        .map(|_| rng.gen_range(1..(num_elements * 10) as i32))
        .collect();

    // --- Build ---
    let build_start = Instant::now();
    let tree = ConcTreeList::from_vec(elements.clone());
    let build_time = build_start.elapsed().as_secs_f64();

    // --- Search ---
    let search_indices: Vec<usize> = (0..100)
        .map(|_| rng.gen_range(0..tree.len().max(1)))
        .collect();
    let search_time = measure_time(|| {
        for &idx in &search_indices {
            let _ = tree.get(idx);
        }
    });

    // --- Delete_at ---
    // Clone the tree and perform up to 100 deletions.
    let delete_at_time = measure_time(|| {
        let mut t = tree.clone();
        for _ in 0..100 {
            if t.len() == 0 {
                break;
            }
            let idx = rng.gen_range(0..t.len());
            t = t.delete_at(idx);
        }
    });

    // --- Insert_at ---
    // Clone the tree and perform 100 insertions at random indices.
    let insert_at_time = measure_time(|| {
        let mut t = tree.clone();
        for _ in 0..100 {
            let idx = rng.gen_range(0..=t.len());
            let value = rng.gen_range(1..(num_elements * 10) as i32);
            t = t.insert_at(idx, value);
        }
    });

    // --- Append ---
    // Clone the tree and perform 100 append operations.
    let append_time = measure_time(|| {
        let mut t = tree.clone();
        for _ in 0..100 {
            t = t.concat(ConcTreeList::single(rng.gen_range(1..(num_elements * 10) as i32)));
        }
    });

    BenchmarkResult {
        elements: num_elements,
        build_time,
        search_time,
        delete_at_time,
        insert_at_time,
        append_time,
    }
}

/// Prints the benchmark results in table form.
fn print_table(results: &[BenchmarkResult]) {
    println!(
        "{:<10} {:<12} {:<12} {:<12} {:<12} {:<12}",
        "Elements", "Build(s)", "Search(s)", "Delete(s)", "Insert(s)", "Append(s)"
    );
    for res in results {
        println!(
            "{:<10} {:<12.6} {:<12.6} {:<12.6} {:<12.6} {:<12.6}",
            res.elements,
            res.build_time,
            res.search_time,
            res.delete_at_time,
            res.insert_at_time,
            res.append_time,
        );
    }
}

/// Plots a combined graph with all operations.
fn plot_combined_results(results: &[BenchmarkResult]) -> Result<(), Box<dyn std::error::Error>> {
    use plotters::prelude::*;

    let root = BitMapBackend::new("benchmark_combined.png", (1280, 720)).into_drawing_area();
    root.fill(&WHITE)?;

    let max_elements = results.iter().map(|r| r.elements).max().unwrap_or(0);
    let max_time = results
        .iter()
        .flat_map(|r| vec![
            r.build_time,
            r.search_time,
            r.delete_at_time,
            r.insert_at_time,
            r.append_time,
        ])
        .fold(0.0, f64::max);

    let mut chart = ChartBuilder::on(&root)
        .caption("ConcTreeList Benchmark (Combined)", ("sans-serif", 40))
        .margin(10)
        .x_label_area_size(40)
        .y_label_area_size(60)
        .build_cartesian_2d(0usize..max_elements, 0f64..max_time)?;

    chart.configure_mesh().draw()?;

    // Plot each series.
    chart
        .draw_series(LineSeries::new(
            results.iter().map(|r| (r.elements, r.build_time)),
            &RED,
        ))?
        .label("Build")
        .legend(|(x, y)| PathElement::new([(x, y), (x + 20, y)], &RED));

    chart
        .draw_series(LineSeries::new(
            results.iter().map(|r| (r.elements, r.search_time)),
            &BLUE,
        ))?
        .label("Search")
        .legend(|(x, y)| PathElement::new([(x, y), (x + 20, y)], &BLUE));

    chart
        .draw_series(LineSeries::new(
            results.iter().map(|r| (r.elements, r.delete_at_time)),
            &GREEN,
        ))?
        .label("Delete_at")
        .legend(|(x, y)| PathElement::new([(x, y), (x + 20, y)], &GREEN));

    chart
        .draw_series(LineSeries::new(
            results.iter().map(|r| (r.elements, r.insert_at_time)),
            &CYAN,
        ))?
        .label("Insert_at")
        .legend(|(x, y)| PathElement::new([(x, y), (x + 20, y)], &CYAN));

    chart
        .draw_series(LineSeries::new(
            results.iter().map(|r| (r.elements, r.append_time)),
            &AMBER,
        ))?
        .label("Append")
        .legend(|(x, y)| PathElement::new([(x, y), (x + 20, y)], &AMBER));

    chart.configure_series_labels().border_style(&BLACK).draw()?;

    println!("Combined graph saved as 'benchmark_combined.png'");
    Ok(())
}

/// Plots an individual graph for a given operation.
/// The extractor closure returns the time for a given BenchmarkResult.
fn plot_individual_results<F>(
    results: &[BenchmarkResult],
    title: &str,
    y_label: &str,
    extractor: F,
    output_file: &str,
    color: &RGBColor,
) -> Result<(), Box<dyn std::error::Error>>
where
    F: Fn(&BenchmarkResult) -> f64,
{
    use plotters::prelude::*;

    let root = BitMapBackend::new(output_file, (1280, 720)).into_drawing_area();
    root.fill(&WHITE)?;

    let max_elements = results.iter().map(|r| r.elements).max().unwrap_or(0);
    let max_time = results.iter().map(|r| extractor(r)).fold(0.0, f64::max);

    let mut chart = ChartBuilder::on(&root)
        .caption(title, ("sans-serif", 40))
        .margin(10)
        .x_label_area_size(40)
        .y_label_area_size(60)
        .build_cartesian_2d(0usize..max_elements, 0f64..max_time)?;

    chart.configure_mesh().draw()?;

    chart
        .draw_series(LineSeries::new(
            results.iter().map(|r| (r.elements, extractor(r))),
            color,
        ))?
        .label(y_label)
        .legend(|(x, y)| PathElement::new([(x, y), (x + 20, y)], color));

    chart.configure_series_labels().border_style(&BLACK).draw()?;
    println!("Graph '{}' saved as '{}'", title, output_file);
    Ok(())
}

fn main() {
    // Parse command-line arguments.
    let args = Args::parse();

    // Determine the range of sizes to evaluate.
    let sizes: Vec<usize> = if let Some(end) = args.end {
        let steps = args.steps.max(2);
        let step = (end - args.start) / (steps - 1);
        (0..steps).map(|i| args.start + i * step).collect()
    } else {
        vec![args.start]
    };

    // Run the benchmark for each size sequentially.
    let mut results: Vec<BenchmarkResult> = Vec::new();
    for size in sizes {
        println!("Running benchmark for {} elements...", size);
        results.push(benchmark_operations(size));
    }

    // If the table option is set, print the results.
    if args.table {
        print_table(&results);
    }

    // If the plot option is set, generate graphs.
    if args.plot {
        // Combined graph.
        if let Err(e) = plot_combined_results(&results) {
            eprintln!("Error generating combined graph: {}", e);
        }
        // Individual graphs.
        if let Err(e) = plot_individual_results(
            &results,
            "Build Time",
            "Build (s)",
            |r| r.build_time,
            "benchmark_build.png",
            &RED,
        ) {
            eprintln!("Error generating build graph: {}", e);
        }
        if let Err(e) = plot_individual_results(
            &results,
            "Search Time",
            "Search (s)",
            |r| r.search_time,
            "benchmark_search.png",
            &BLUE,
        ) {
            eprintln!("Error generating search graph: {}", e);
        }
        if let Err(e) = plot_individual_results(
            &results,
            "Delete_at Time",
            "Delete_at (s)",
            |r| r.delete_at_time,
            "benchmark_delete.png",
            &GREEN,
        ) {
            eprintln!("Error generating delete graph: {}", e);
        }
        if let Err(e) = plot_individual_results(
            &results,
            "Insert_at Time",
            "Insert_at (s)",
            |r| r.insert_at_time,
            "benchmark_insert.png",
            &CYAN,
        ) {
            eprintln!("Error generating insert graph: {}", e);
        }
        if let Err(e) = plot_individual_results(
            &results,
            "Append Time",
            "Append (s)",
            |r| r.append_time,
            "benchmark_append.png",
            &AMBER,
        ) {
            eprintln!("Error generating append graph: {}", e);
        }
    }
}
