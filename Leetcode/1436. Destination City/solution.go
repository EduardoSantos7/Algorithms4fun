func destCity(paths [][]string) string {
	visited := make(map[string]string, len(paths)*2) // New empty set

	for _, cities := range paths {
		visited[cities[0]] = "s"
		if _, ok := visited[cities[1]]; !ok {
			visited[cities[1]] = ""
		}
	}

	// Get the difference (end - start)
	for city, value := range visited {
		if value == "" {
			return city
		}
	}

	return ""
}