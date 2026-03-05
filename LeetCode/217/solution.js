var containsDuplicate = function(nums) {
    set_nums = new Set(nums);

    if (set_nums.size == nums.length) {
        return false;
    }

    return true;
};