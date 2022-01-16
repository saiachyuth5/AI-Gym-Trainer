# AI-Gym-Trainer
The idea behind the project is to utilize pose
estimation to effectively analyse workouts and
provide visual cues to correct the posture during
workouts to prevent long term injuries, muscular
imbalances and also engage the muscles
effectively for a proper workout. In this project I
have explored the mediapipe platform from
google and utilised its pose estimation
framework to track a single workout and derive
various insights.I have also explored various
applications of pose estimation which I have
summarized in the applications and future work
section.
# Introduction
Human body pose estimation from real-time
videos or images plays a central role in various
applications such as health tracking, body
language detection, and gestural control.It is a
very challenging task and we have to deal with a
number of variables such as the large number of
poses ,different body sizes, numerous degrees of
freedom, and part occlusions.
Pose estimation was originally done using
pictorial structures which model the human body
as a collection of rigid templates and a set of
pairwise potentials which form a tree structure
allowing for efficient inference at test time.
Recently , with the advent of neural networks ,
Convolutional Neural Networks have shown
remarkable and robust performance and high
part localization accuracy which outperform
prior methods by a large margin. A key feature
of these approaches is that they integrate
non-linear hierarchical feature extraction with
regression and make use of the large datasets
that are readily available. For human pose
estimation , the CNN features are regressed in
order to provide joint prediction of the body
parts.

# Mediapipe Framework
Mediapipe is a user-friendly and easy to use
framework which provides a number of
functionalities such as pose estimation , iris
recognition , hand gesture recognition etc. The
pose estimation functionality utilizes a two step
detector-tracker pipeline which was proven to be
effective in a number of other applications. The
detector first locates the person region of interest
(ROI) within the frame. The BlazeFace model is
used as a proxy for a person detector and hence
this model comes with an assumption that the
person’s face is visible in the frame which is the
case for most of the mobile devices. The tracker
then uses this pose alignment to subsequently
predict the pose landmarks and keypoint
coordinates, and redefines the region of interest
for the current frame. When the person moves
out of frame or the face is not visible then the
detector network is re-run to estimate the pose
alignment

# BlazePose - Model and Architecture
The common approach for pose estimation
involves producing heatmaps for all joints along
with refining offsets over each coordinate.While
this is a good and scalable technique , it is too
heavy for single person pose estimation or to run
on a mobile device. In contrast , regression
based techniques are less computationally
demanding and are also equally scalable.
BlazePose uses a stacks hourglass architecture
which gives a significant boost to the quality of
prediction even with a small number of
parameters. A encoder-decoder network
architecture is used to predict the heatmap of all
the joints , which is followed by another
regressor which regresses directly on the
coordinates of all the joints. The heatmap branch
is used only in the training stage and it is
discarded during the inference phase which
results in a lightweight embedding and increase
in performance. This is what makes the network
suitable for mobile devices and CPUS. Skip
connections are actively utilised between
different layers of the network to achieve a
balance between the high level and the low level
features. Also the gradients from the enoder
network are not propagated back to the heatmap
trained features which increases the performance
as well as regression accuracy to a large extent.

