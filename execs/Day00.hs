module Main (main) where
import           Data.Set (Set)
import qualified Data.Set as Set

import           Advent
incrSum []     = []
incrSum (x:xs) = x: map (x+)(incrSum xs)

insert :: Ord a=> a ->[a]->[a]
insert x []     = [x]
insert x (y:ys) | x <= y = x:y:ys
                | otherwise = y : insert x ys

isort :: Ord a => [a] -> [a]
isort []     = []
isort (x:xs) = insert x (isort xs)


main :: IO ()
main =
 do inp <- getParsedLines 0 number
    -- Key idea: changes applied are the same, starting number is different,
    let s = incrSum inp
    let freq = s ++ map ((last s)+) freq
    -- print (incrSum inp)
    let repetition = []
    print (take 100000 freq)
    print (last s)
