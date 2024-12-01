#!/usr/bin/env ruby

def char_range(pairs, template)
  numbers = Hash.new(0)
  numbers[template[0]] = 1

  pairs.each_pair do |k, v|
    numbers[k[1]] += v
  end

  values = numbers.values.sort
  values.last - values.first
end

rules = {}
template = ''

File.open('input.txt') do |f|
  template = f.readline.strip
  f.readline

  f.read.each_line do |line|
    pair, element = line.strip.split(' -> ')
    rules.store(pair, element)
  end
end

pairs = Hash.new(0)

(1...template.length).each do |i|
  pair = template[i - 1, 2]
  pairs[pair] += 1
end

40.times do |i|
  puts "Range on 10 iterations (1): #{char_range(pairs, template)}" if i == 10

  new_pairs = Hash.new(0)

  pairs.each_pair do |k, v|
    element = rules[k]
    new_pairs[k[0] + element] += v
    new_pairs[element + k[1]] += v
  end

  pairs = new_pairs
end

puts "Range on 40 iterations (2): #{char_range(pairs, template)}"
