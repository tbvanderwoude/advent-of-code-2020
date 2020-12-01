module Main (main) where

-- import           Advent

main :: IO ()
main =
  do inp <- map read <$> lines <$> readFile "inputs/input01.txt"
     let pairs = [(x,y)|x<-inp,y<-[z|z<-inp,z<=2020-x],x+y==2020]
     let triples = [(x,y,w)|x<-inp,y<-[z|z<-inp,z<=2020-x],w<-[z|z<-inp,z<=2020-y-x],x+y+w==2020]
     print ((\(x,y) -> x*y) (head pairs))
     print ((\(x,y,z) -> x*y*z) (head triples))
