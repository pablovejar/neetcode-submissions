class Solution {
    public boolean hasDuplicate(int[] nums) {
        Set<Integer> setOfNums = Arrays.stream(nums).boxed().collect(Collectors.toCollection(HashSet::new));

        return setOfNums.size() != nums.length;
    }
}