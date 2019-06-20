source("funcs.R")
prod = 1
all_divisors = find_divisors(seq(1, 20))
for(name in names(all_divisors)) {
    prod = prod * as.integer(name)^all_divisors[names(all_divisors) == name]
}

print(as.integer(prod))