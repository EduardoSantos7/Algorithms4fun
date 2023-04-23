use std::collections::HashMap;

impl Solution {
    pub fn is_bipartite(graph: Vec<Vec<i32>>) -> bool {
        let mut colors = HashMap::new();
        let mut queue = Vec::new();

        for root in 0..graph.len() {
            if let Some(x) = colors.get(&(root as i32)) {
                continue;
            }

            colors.insert(root as i32, 0);
            queue.push(root as i32);

            while queue.len() != 0 {
                if let Some(vertice) = queue.pop() {
                    let edges = &graph[vertice as usize];

                    for &edge in edges {
                        if let Some(x) = colors.get(&edge) {
                            if let Some(y) = colors.get(&vertice) {
                                if x == y {
                                    return false;
                                }
                            }
                        } else {
                            queue.push(edge);
                            colors.insert(edge, 1 - colors[&vertice]);
                        }
                    }
                }
            }
        }

        true
    }
}
