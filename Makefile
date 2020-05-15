
train:
	./darknet detector train train-dogcat/cat-dog-obj.data train-dogcat/network-architecture.cfg train-dogcat/darknet53.conv.74

init:
	wget https://pjreddie.com/media/files/darknet53.conv.74 train-dogcat/

get_weigth_file:
	ssh jc@10.0.10.5 "cp /home/jc/jcdarknet/train-dogcat/weights/network-architecture_last.weights /home/jc"
	scp jc@10.0.10.5:/home/jc/network-architecture_last.weights model.weights
