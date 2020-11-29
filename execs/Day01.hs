module Main (main) where

import           Advent

main :: IO ()
main =
  do inp <- getParsedLines 1 number
     print (inp)
