import streamlit as st
import streamlit.components.v1 as components

from utils.function_call import *
from utils.deployment import *

opt = st.sidebar.selectbox("",("Home", "Resources", "Visualizer"))

#lrn = st.sidebar.button("Learn More")

#if lrn:
#        clf = st.checkbox("Classification")
#        if clf:
#            st.write("ABC")
#try:

if opt == "Home":

    #st.set_page_config(layout='wide')

    html_temp = '''
        <div>
        <h2></h2>
        <center><h3>Vision Dashboard - A One-Stop CV Learning Tool</h3></center>
        </div>
        '''

    
    st.markdown(html_temp, unsafe_allow_html=True)
    
    tree()
    st.header("")

    carousel()

elif opt == "Resources":

    html_temp = '''
        <div>
        <h2></h2>
        <center><h3>Resources</h3></center>
        </div>
        '''

    st.markdown(html_temp, unsafe_allow_html=True)

    clf = st.checkbox("Image Classification")

    if clf:

        """
        Image Classification is the process of categorizing and labeling groups of pixels or vectors within an image based on specific rules.

        """

    det = st.checkbox("Detection")
    
    if det:

        """
        Detection is a computer vision technique that allows us to identify and locate something in an image or video.

        """

    seg = st.checkbox("Segmentation")

    if seg:

        """
        Segmentation is the process of dividing an image into different regions based on the characteristics of pixels to identify objects or boundaries to simplify an image and more efficiently analyze it.

        """

    dns = st.checkbox("Denoising")

    if dns:

        """
        Denoising refers to estimating the original image by suppressing noise from a noise-contaminated version of the image.

        """

    sty = st.checkbox("Style Transfer")

    if sty:

        """
        Style transfer is a computer vision technique that takes two images—a content image and a style reference image—and blends them together so that the resulting output image retains the core elements of the content image, but appears to be “painted” in the style of the style reference image.

        """

    srg = st.checkbox("Super Resolution")

    if srg:

        """
        Super-resolution is based on the idea that a combination of low resolution (noisy) sequence of images of a scene can be used to generate a high resolution image or image sequence. Thus it attempts to reconstruct the original scene image with high resolution given a set of observed images at lower resolution.
        """

else:

    task = st.sidebar.selectbox("Select the Algorithm that you want to run!",("Classification", "Face Detection", "Object Detection", "Instance Segmentation", "Semantic Segmentation", "Denoising", "Style Transfer", "Super Resolution"))

    input_image = image_upload()
    #st.image(input_image, width = 300, caption = 'Uploaded Image')

    if input_image is not None:

        if task == "Classification":

            output = classify(input_image)

            if st.button("Classify"):
                display(input_image, captions=['Uploaded Image'])
                st.success("The Uploaded Image has been Classified as '{}'".format(output))
                
        elif task == "Face Detection":
            
            try:
                output = face_detect(input_image)

                if st.button("Detect Face"):
                    display(input_image, captions=['Uploaded Image', 'Face(s) Detected!'], resimg=output)

            except:
                st.info("No Face(s) present in Uploaded Image! Please upload an Image having human face(s) to detect.")

        elif task == "Object Detection":
            
            output = object_detect(input_image)

            if st.button("Detect Object"):
                display(input_image, captions=['Uploaded Image', 'Object(s) Detected!'], resimg=output)

        elif task == "Instance Segmentation":

            output = instance_segment(input_image)

            if st.button("Segment"):
                display(input_image, captions=['Uploaded Image', 'Image Segmented!'], resimg=output)

        elif task == "Semantic Segmentation":

            output = semantic_segment(input_image)

            if st.button("Segment"):
                display(input_image, captions=['Uploaded Image', 'Image Segmented!'], resimg=output)

        elif task == "Denoising":
            
            noise = st.radio("Please Select a Noise type",("text","gaussian"))
            output = denoise(input_image, noise)

            if st.button("Denoise"):
                display(input_image, captions=['Uploaded Image', 'Image Denoised!'], resimg=output)

        elif task == "Style Transfer":

            style = st.radio("Please Select a Style Image", ("candy", "mosaic", "rain_princess", "udnie"))
            
            style_image = Image.open("misc/images/style_images/{}.jpg".format(style))
            
            # Hacky way to centre image
            col1, col2, col3 = st.columns([4,10,4])
            
            with col1:
                st.write("")
            with col2:
                st.image(style_image, width=300)
            with col3:
                st.write("")

            style_image = style_image.resize((input_image.size))
            output = transfer(input_image, style)

            if st.button("Transfer Style"):
                display(input_image, captions=['Content Image', 'Style Image'], resimg=style_image)
                st.image(output, width=660, caption="Stylized Image!")

        elif task == "Super Resolution":
            output = superres(input_image)
            
            if st.button("Transform"):
                display(input_image, captions=['Uploaded Image', 'Image Transformed!'], resimg=output)

