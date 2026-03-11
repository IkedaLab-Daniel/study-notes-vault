var bitwiseComplement = function(n) {
    const bin_n = n.toString(2)
    let rev_bin_n = ""

    for (let i = 0; i < bin_n.length; i++) {
        if (bin_n[i] == "1") {
            rev_bin_n += "0"
        } else {
            rev_bin_n += "1"
        }
    }

    const final_int = parseInt(rev_bin_n, 2)

    return final_int

};

console.log(bitwiseComplement(5))