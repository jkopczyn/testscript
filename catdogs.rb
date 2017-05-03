#!/usr/bin/ruby
def catdogs
    (1..100).each do |n|
        if n % 15 == 0
            puts "Cats&Dogs"
        elsif n % 3 == 0
            puts "Cats"
        elsif n % 5 == 0
            puts "Dogs"
        else
            puts n
        end
    end
end

catdogs()
