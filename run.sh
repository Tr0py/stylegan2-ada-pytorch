for i in $(seq 0 9); do
	echo "generating images for Class $i"
	python generate.py --outdir=cifar-10-$i --seeds=0-2000 --class=$i \
		    --network=https://nvlabs-fi-cdn.nvidia.com/stylegan2-ada-pytorch/pretrained/cifar10.pkl
done
