echo "installing requirements"
pip install -r ./requirements.txt

for i in $(seq 0 9); do
	echo "generating images for Class $i"
	python generate.py --outdir=cifar-10-$i --seeds=0-2000 --class=$i \
		    --network=https://nvlabs-fi-cdn.nvidia.com/stylegan2-ada-pytorch/pretrained/cifar10.pkl
	echo "output is saved in cifar-10-$i"
done

tar -czvf cifar-10.tar.gz cifar-10-*
echo "output is saved in cifar-10.tar.gz"
