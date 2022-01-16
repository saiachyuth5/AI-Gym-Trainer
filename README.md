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


