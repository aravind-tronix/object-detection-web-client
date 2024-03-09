import numpy as np
import time
import os


def open_read_image(filename):
    import cv2

    labelsPath = "./CustomConfigs/obj.names"
    LABELS = open(labelsPath).read().strip().split("\n")

    # initialize a list of colors to represent each possible class label
    np.random.seed(42)
    COLORS = np.random.randint(0, 255, size=(len(LABELS), 3), dtype="uint8")

    # derive the paths to the YOLO weights and model configuration
    # give path where you have stored yolov3.weights file and rename the file as yolov3
    weightsPath = "count.weights"

    # give path where you have stored yolov3.cfg file and rename the file as yolov3
    configPath = "./CustomConfigs/custom.cfg"

    # load our YOLO object detector trained on COCO dataset
    net = cv2.dnn.readNetFromDarknet(configPath, weightsPath)

    # load our input image and grab its spatial dimensions
    image = cv2.imread(filename)
    (H, W) = image.shape[:2]

    # determine only the *output* layer names that we need from YOLO
    ln = net.getLayerNames()
    ln = [ln[i[0] - 1] for i in net.getUnconnectedOutLayers()]

    # construct a blob from the input image and then perform a forward
    # pass of the YOLO object detector, giving us our bounding boxes and
    # associated probabilities
    blob = cv2.dnn.blobFromImage(image, 1 / 255.0, (416, 416),
                                 swapRB=True, crop=False)
    net.setInput(blob)
    start = time.time()
    layerOutputs = net.forward(ln)
    end = time.time()

    # show timing information on YOLO

    # initialize our lists of detected bounding boxes, confidences, and
    # class IDs, respectively
    boxes = []
    confidences = []
    classIDs = []

    # loop over each of the layer outputs
    for output in layerOutputs:
        # loop over each of the detections
        for detection in output:
            # extract the class ID and confidence (i.e., probability) of
            # the current object detection
            scores = detection[5:]
            classID = np.argmax(scores)
            confidence = scores[classID]

            # filter out weak predictions by ensuring the detected
            # probability is greater than the minimum probability
            if confidence > 0.3:
                # scale the bounding box coordinates back relative to the
                # size of the image, keeping in mind that YOLO actually
                # returns the center (x, y)-coordinates of the bounding
                # box followed by the boxes' width and height
                box = detection[0:4] * np.array([W, H, W, H])
                (centerX, centerY, width, height) = box.astype("int")

                # use the center (x, y)-coordinates to derive the top and
                # and left corner of the bounding box
                x = int(centerX - (width / 2))
                y = int(centerY - (height / 2))

                # update our list of bounding box coordinates, confidences,
                # and class IDs
                boxes.append([x, y, int(width), int(height)])
                confidences.append(float(confidence))
                classIDs.append(classID)

    # apply non-maxima suppression to suppress weak, overlapping bounding
    # boxes
    idxs = cv2.dnn.NMSBoxes(boxes, confidences, 0.3, 0.3)

    # count the number of persons

    # ensure at least one detection exists
    if len(idxs) > 0:
        count = []
        repeat = []
        result = []
        # loop over the indexes we are keeping
        for i in idxs.flatten():
            count.append(LABELS[classIDs[i]])
            # print(count)
            # print(i.countnt(LABELS[classIDs[i]]))
        for data in count:
            if data not in repeat:
                repeat.append(data)
                result.append(data+(str(count.count(data))))
    else:
        result = []
        result.append("cant determined you object")

    os.remove(filename)
    # cv2.imwrite(filename+"_out.jpg", image)
    image = None
    idxs = None
    net = None
    COLORS = None
    classIDs = None
    confidences = None
    boxes = None
    cv2 = None
    layerOutputs = None
    return result
