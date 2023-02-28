const getCombinations = (length, selectNumber) => {
  const dfs = (start, depth, arr, result) => {
    if (depth === selectNumber) {
      result.push(arr.slice(0, selectNumber));
      return;
    }

    for (let i = start; i < length; i++) {
      arr[depth] = i;
      dfs(i + 1, depth + 1, arr, result);
    }
  }

  const combinations = [];
  const arr = Array.from({ length }, (_, i) => i);
  dfs(0, 0, arr, combinations);
  return combinations;
}

const isMinimality = (uniqueKeys, combination) =>
  !uniqueKeys.some((uniqueKey) => uniqueKey.every((v) => combination.includes(v)));

const isUnique = (relation, combination) =>
  new Set(relation.map((row) => combination.map((index) => row[index]).join(''))).size === relation.length;


const solution = (relation) => {
  const uniqueKeys = [];

  const columns = relation[0].length;

  Array.from(Array(columns), (_, i) => i + 1).map((i) =>
    getCombinations(columns, i)
      .filter((combination) => isMinimality(uniqueKeys, combination))
      .filter((combination) => isUnique(relation, combination))
      .forEach((combination) => uniqueKeys.push(combination)));

  return uniqueKeys.length;
}

console.log(solution([["100","ryan","music","2"],["200","apeach","math","2"],["300","tube","computer","3"],["400","con","computer","4"],["500","muzi","music","3"],["600","apeach","music","2"]]));