def bitwiseComplement(n: int) -> int:
        bin_n = bin(n)
        str_bin_n = str(bin_n)
        reversed_str_bin_n = ""

        for i in range(2, len(str_bin_n)):
            if str_bin_n[i] == "0":
                reversed_str_bin_n += "1"
            else:
                reversed_str_bin_n += "0"

        final_int = int(("0b" + reversed_str_bin_n), 2)

        return final_int

print(bitwiseComplement(5))