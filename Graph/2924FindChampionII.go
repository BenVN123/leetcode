func findChampion(n int, edges [][]int) int {
	weaker := make([]bool, n)

	for _, v := range edges {
		if !weaker[v[1]] {
			weaker[v[1]] = true
		}
	}

	champion := -1
	for i, v := range weaker {
		if !v {
			if champion != i {
				if champion != -1 {
					return -1
				} else {
					champion = i
				}
			}
		}
	}

	return champion
}
