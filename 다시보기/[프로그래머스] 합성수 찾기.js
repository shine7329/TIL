function solution(n) {
	let result = 0;
	for (let i = 2; i <= n; i++) {
		const sqrt = Math.sqrt(i);
		for (let j = 2; j <= sqrt; j++) {
			if (i % j) continue;
			console.log(i);
			result += 1;
			break
		}
	}
	return result;
}

console.log(solution(15));
