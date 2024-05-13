import cv2
import numpy as np

class Precompositions:
    # def Pre1_Saturate(self, frame):
    #     hsv_image = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    #     saturation_factor = 1.75
    #     hsv_image[:, :, 1] = np.clip(hsv_image[:, :, 1] * saturation_factor, 0, 255).astype(np.uint8)
    #     saturated_image = cv2.cvtColor(hsv_image, cv2.COLOR_HSV2BGR)
    #     return saturated_image

    def Pre0_Resize(self, frame):
        height, width = frame.shape[:2]
        border_size = 150   
        cropped_image = frame[border_size:height-border_size, border_size:width-border_size]
        return cropped_image


    # def Pre2(self, frame, factor = 0.8):
    #     hsv_image = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    #     hue_channel = hsv_image[:, :, 0]

    
    #     mean_hue = np.mean(hue_channel)
    #     hue_diff = hue_channel - mean_hue

    #     hue_diff = hue_diff * factor

    #     hsv_image[:, :, 0] = (hue_channel + hue_diff) % 180
    #     frame = cv2.cvtColor(hsv_image, cv2.COLOR_HSV2BGR)
    #     return frame


    def Pre3(self, frame, factor = 4):
        pass


    def Pre4(self, frame):
        pass



class RenderTasks:
    def R1(self, frame, factor = 4):
        hsv_image = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

        hue_channel = hsv_image[:, :, 0]
        mean_hue = np.mean(hue_channel)

        diff = hue_channel - mean_hue
        hue_channel = hue_channel + diff * factor
        hsv_image[:, :, 0] = hue_channel

        frame = cv2.cvtColor(hsv_image, cv2.COLOR_HSV2BGR)
        # hue_difference = (hue_channel - mean_hue)

        # normalized_difference = hue_difference / np.max(hue_difference) * 255
        
        # threshold = 15
        # highlighted_image = np.copy(frame)
        # highlighted_image[normalized_difference > threshold] = (255, 0, 0)
        return frame
    
    def R2(self, frame):
        hsv_image = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        
        hue_channel = hsv_image[:, :, 0]
        mean_hue = np.mean(hue_channel)
        mod_mean = mean_hue / (-7)

        hsv_image[:, :, 0] = np.where(hue_channel-mean_hue < mod_mean ,hue_channel%20 , hue_channel)
        frame = cv2.cvtColor(hsv_image, cv2.COLOR_HSV2BGR)
        return frame
    
    
class Postcompositions:
    def P1(self, frame):
        return frame
    
    def P2(self, frame):
        return frame
    