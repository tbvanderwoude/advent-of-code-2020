module Main (main) where
import           Data.Function
import           Data.List
import           Data.Ord
import           Data.Set      (Set)
import qualified Data.Set      as Set

import           Advent
incrSum []     = []
incrSum (x:xs) = x: map (x+)(incrSum xs)

diffCongr ::  Int->Int->Int->Bool
diffCongr x y m = ((mod (y-x) m) == 0) && (y-x)<0

firstOfThree (c,_,_) = c
mySort xs = sortBy (comparing firstOfThree) xs


main :: IO ()
main =
 do inp <- getParsedLines 0 number
    -- Key idea: changes applied are the same, starting number is different,
    let s = incrSum inp
    -- let freq = s ++ map ((last s)+) freq
    -- let samples = take 100000 freq
    -- let singleDup = [x|x<-(tail samples), x==head samples]
    -- let dupsAhead xs | null xs = []
    --                  | otherwise = [x|x<-(tail xs), x==head xs] ++ dupsAhead (tail xs)
    print s
    let test = [(div (x-y) (last s),x,y) | (xi,x)<-zip [0..((length s) - 1)] s, (yi,y)<-zip [0..((length s) - 1)] s,diffCongr x y (last s),xi/=yi]
    -- print (take 10000 freq)
    -- print (head (dupsAhead samples))
    print test
    print (mySort test)
