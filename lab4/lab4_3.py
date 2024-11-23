import cv2
import argparse


def main():
    parser = argparse.ArgumentParser(prog='Video cutter')
    parser.add_argument('-i', '--input', help='Путь до файла')

    args = parser.parse_args()

    cap = cv2.VideoCapture(args.input)
    fps = cap.get(cv2.CAP_PROP_FPS)
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        font = cv2.FONT_HERSHEY_SIMPLEX
        cv2.putText(frame,  
                args.input,  
                (50, 50),  
                font, 1,  
                (0, 255, 255),  
                2,  
                cv2.LINE_4) 
        cv2.putText(frame,  
                str(fps),  
                (50, 100),  
                font, 1,  
                (0, 255, 255),  
                2,  
                cv2.LINE_4) 
        
        cv2.imshow('video', frame) 
        if cv2.waitKey(1) & 0xFF == ord('q'): 
            break
        
    cap.release() 
    cv2.destroyAllWindows() 

if __name__ == '__main__':
    main()

# python3 lab4/lab4_3.py -i lab4/video.mp4