type void struct{}

var member void

func destCity(paths [][]string) string {
	start := make(map[string]void, len(paths)) // New empty set

	for _, cities := range paths {
		start[cities[0]] = member
	}

	// Get the difference (end - start)
	for _, cities := range paths {
		if _, ok := start[cities[1]]; !ok {
			return cities[1]
		}
	}

	return ""
}