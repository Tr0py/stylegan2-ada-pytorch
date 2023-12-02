for i in $(seq 1 10); do
	python generate.py --outdir=cifar-10-$i --seeds=0-50 --class=$i \
		    --network=https://nvlabs-fi-cdn.nvidia.com/stylegan2-ada-pytorch/pretrained/cifar10.pkl
done
