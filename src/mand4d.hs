--Mandelbrot set in 4 dimensions
import Codec.Picture
import Data.Colour.RGBSpace
import Data.Colour.RGBSpace.HSV
import Data.Complex
import Data.List (unfoldr)

data Q = Q Double Double Double Double

plus (Q a b c d) (Q e f g h) = Q (a+e) (b+f) (c+g) (d+h)

quatMult (Q a b c d) (Q e f g h) = Q r i j k
  where r = a*e - b*f - c*g - d*h
        i = a*f + b*e + c*h - d*g
        j = a*g + c*e - b*h + d*f
        k = a*h + d*e + b*g - c*f

dihedMult (Q a b c d) (Q e f g h) = Q r i j k
  where r = a*e - b*f + c*g + d*h
        i = a*f + b*e + c*h - d*g
        j = a*g + c*e + b*h - d*f
        k = a*h + d*e - b*g + c*f

tripleCompMult (Q a b c d) (Q e f g h) = Q r i j k
  where r = a*e - b*f - c*g - d*h
        i = a*f + b*e + c*h + d*g
        j = a*g + c*e + b*h + d*f
        k = a*h + d*e + b*g + c*f

tripleSplitMult (Q a b c d) (Q e f g h) = Q r i j k
  where r = a*e + b*f + c*g + d*h
        i = a*f + b*e + c*h + d*g
        j = a*g + c*e + b*h + d*f
        k = a*h + d*e + b*g + c*f

comp2split1Mult (Q a b c d) (Q e f g h) = Q r i j k
  where r = a*e - b*f - c*g + d*h
        i = a*f + b*e + c*h + d*g
        j = a*g + c*e + b*h + d*f
        k = a*h + d*e - b*g - c*f

comp1split2Mult (Q a b c d) (Q e f g h) = Q r i j k
  where r = a*e - b*f + c*g + d*h
        i = a*f + b*e - c*h - d*g
        j = a*g + c*e - b*h - d*f
        k = a*h + d*e + b*g + c*f

antidihedralMult (Q a b c d) (Q e f g h) = Q r i j k
  where r = a*e + b*f - c*g - d*h
        i = a*f + b*e + c*h + d*g
        j = a*g + c*e - b*h - d*f
        k = a*h + d*e - b*g - c*f

eightMult (Q a b c d) (Q e f g h) = Q r i j k
  where r = a*e - b*f + c*h + d*g
        i = a*f + b*e + c*g - d*h
        j = a*g + c*e + b*h + d*f
        k = a*h + d*e - b*g - c*f

squarerotMult (Q a b c d) (Q e f g h) = Q r i j k
  where r = a*e + b*f + c*h + d*g
        i = a*f + b*e + c*g + d*h
        j = a*g + c*e + b*h + d*f
        k = a*h + d*e + b*g + c*f

antiEightMult (Q a b c d) (Q e f g h) = Q r i j k
  where r = a*e - b*f + c*h - d*g
        i = a*f + b*e + c*g + d*h
        j = a*g + c*e - b*h + d*f
        k = a*h + d*e - b*g - c*f

negiDihedralMult (Q a b c d) (Q e f g h) = Q r i j k
  where r = a*e + b*f - c*g - d*h
        i = a*f + b*e + c*h - d*g
        j = a*g + c*e + b*h - d*f
        k = a*h + d*e + b*g - c*f

negiQuatMult (Q a b c d) (Q e f g h) = Q r i j k
  where r = a*e + b*f + c*g + d*h
        i = a*f + b*e + c*h - d*g
        j = a*g + c*e - b*h + d*f
        k = a*h + d*e + b*g - c*f

norm2 (Q a b c d) = a^2 + b^2 + c^2 + d^2
staysmall tol = (\b -> if b then 1 else 0) . (>=tol) . norm2

--mandelbrot set for multiplication `mult`, iteration count `n` tolerance radius `tol`
mandel mult n tol c = sum $ take n $ map (staysmall tol) $ iterate (\z -> (z `mult` z) `plus` c) c

--convert a+bi to 4-tuple
colorComplex f z = Q r i (h / 90) (s*4 - 2)
  where (h, s) = f z
        r = realPart z
        i = imagPart z

inferno_cmap = map (\[r,g,b] -> PixelRGB8 r g b) [
  [1, 0, 4],
  [48, 7, 84],
  [105, 15, 111],
  [158, 40, 100],
  [208, 72, 67],
  [239, 125, 21],
  [242, 194, 35],
  [245, 255, 163]]

--double compose
dc = (.) . (.)

--converts RGB to pixel RGB values
rgbF8 (RGB r g b)  = PixelRGB8 r' g' b'
  where [r',g',b'] = map (round . (255*)) [r,g,b]

--translate image coordinates x, y to a region of the complex plane
translateComplex imw imh al au bl bu x y = (realfrac + fromIntegral al) :+ (-imagfrac - fromIntegral bl)
  where wfrac = (fromIntegral x) / (fromIntegral imw)
        hfrac = (fromIntegral y) / (fromIntegral imh)
        realfrac = wfrac * (fromIntegral $ au - al)
        imagfrac = hfrac * (fromIntegral $ bu - bl)

--all colorations i'll be using
colorations :: Complex Double -> [(Double, Double)]
colorations z    = [(90*r, (i + 2)/4), (90*i, (r + 2)/4), (90*i, (i + 2)/4), (th * 180/pi, maxnorm'/2)]
  where th       = snd $ polar z
        maxnorm' = maxnorm z
        (r :+ i) = z

--and their names
colorNames = ["i j", "j i", "j j", "polar"]

hs (a, b) = hsv a b 1

maxnorm (a :+ b) = max (abs a) (abs b)

allexamples w h name = mapM_ writer colors'
  where colors'    = zip colorNames $ map (\i -> (!! i) . colorations) [0..]
        complex' c = (rgbF8 . hs . c) `dc` translateComplex w h (-2) 2 (-2) 2
        writer (n,f) = writePng (name' n) $ generateImage (complex' f) w h
        name' x = name ++ x ++ ".png"

qmandel mult = (inferno_cmap !!) . mandel mult 7 16

mandel4d w h f mult = generateImage ((qmandel mult . colorComplex f) `dc` square') w h
  where square' = translateComplex w h (-2) 2 (-2) 2

allfour mult name = mapM_ (\(n,f) -> writePng (name' n) $ mandel4d 512 512 f mult) colors'
  where colors'    = zip colorNames $ map (\i -> (!! i) . colorations) [0..]
        name' x = name ++ x ++ ".png"
