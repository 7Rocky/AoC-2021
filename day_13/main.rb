#!/usr/bin/env ruby

require 'set'

points = Set[]
folds = []
length = 'fold along '.length

File.open('input.txt') do |f|
  x = f.readline.strip

  until x.empty?
    points.add(x)
    x = f.readline.strip
  end

  f.read.each_line do |line|
    axis = line[length, 1]
    fold = line[length + 2..].to_i
    folds.push((axis == 'x' ? 1 : -1) * fold)
  end
end

folds.each_with_index do |fold, i|
  new_points = Set[]

  points.each do |p|
    x, y = p.split(',').map(&:to_i)
    x = fold.positive? && x > fold ? (2 * fold) - x : x
    y = fold.negative? && y > -fold ? (-2 * fold) - y : y
    new_points.add("#{x},#{y}")
  end

  points = new_points
  puts "Number of points after first fold (1): #{points.length}" if i.zero?
end

x = points.map { |p| p.split(',').first.to_i }
y = points.map { |p| p.split(',').last.to_i }

def draw_points(points, max_x, max_y)
  origami = ''

  (0..max_y).each do |y|
    (0..max_x).each do |x|
      origami += points.include?("#{x},#{y}") ? '#' : '.'
    end

    origami += "\n"
  end

  origami
end

puts 'Hidden message (2):', draw_points(points, x.max, y.max)
