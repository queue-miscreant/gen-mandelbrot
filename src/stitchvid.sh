ffmpeg \
	-i "slices $1 1.mp4" -i "slices $1 j.mp4" -i "slices $1 ijk.mp4" -i "slices $1 1jk.mp4" \
	-filter_complex "
		nullsrc=size=640x480 [base];
		[0:v] setpts=PTS-STARTPTS, scale=320x240 [upperleft];
		[1:v] setpts=PTS-STARTPTS, scale=320x240 [upperright];
		[2:v] setpts=PTS-STARTPTS, scale=320x240 [lowerleft];
		[3:v] setpts=PTS-STARTPTS, scale=320x240 [lowerright];
		[base][upperleft] overlay=shortest=1 [tmp1];
		[tmp1][upperright] overlay=shortest=1:x=320 [tmp2];
		[tmp2][lowerleft] overlay=shortest=1:y=240 [tmp3];
		[tmp3][lowerright] overlay=shortest=1:x=320:y=240
	" \
	-c:v libx264 "$1.mp4"
