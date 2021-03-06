import numpy as np
from random import shuffle

def softmax_loss_naive(W, X, y, reg):
  """
  Softmax loss function, naive implementation (with loops)

  Inputs have dimension D, there are C classes, and we operate on minibatches
  of N examples.

  Inputs:
  - W: A numpy array of shape (D, C) containing weights.
  - X: A numpy array of shape (N, D) containing a minibatch of data.
  - y: A numpy array of shape (N,) containing training labels; y[i] = c means
    that X[i] has label c, where 0 <= c < C.
  - reg: (float) regularization strength

  Returns a tuple of:
  - loss as single float
  - gradient with respect to weights W; an array of same shape as W
  """
  # Initialize the loss and gradient to zero.
  loss = 0.0
  dW = np.zeros_like(W)

  #############################################################################
  # TODO: Compute the softmax loss and its gradient using explicit loops.     #
  # Store the loss in loss and the gradient in dW. If you are not careful     #
  # here, it is easy to run into numeric instability. Don't forget the        #
  # regularization!                                                           #
  #############################################################################
  num_train = X.shape[0]  
  
  scores = np.dot(X, W)
#   scores -= max(scores) # 为了数值稳定
  p = np.zeros_like(scores)
  for i in range(num_train):
    exp_scores = np.exp(scores[i])
    e_sum_i = np.sum(exp_scores)
    exp_scores /= e_sum_i
    correct_y = y[i]
    loss += -np.log(exp_scores[correct_y])
    
    for j in range(exp_scores.shape[0]):
        if j != correct_y:
            dW[:,j] += exp_scores[j] * X[i]
        else:
            dW[:,j] -= (1-exp_scores[j]) * X[i]
    
  
  loss /= num_train
  loss += reg * np.sum(W*W)

  dW /= num_train
  dW += 2 * reg * W
        
        
        
        
        
        
        
  #############################################################################
  #                          END OF YOUR CODE                                 #
  #############################################################################

  return loss, dW


def softmax_loss_vectorized(W, X, y, reg):
  """
  Softmax loss function, vectorized version.

  Inputs and outputs are the same as softmax_loss_naive.
  """
  # Initialize the loss and gradient to zero.
  loss = 0.0
  dW = np.zeros_like(W)

  #############################################################################
  # TODO: Compute the softmax loss and its gradient using no explicit loops.  #
  # Store the loss in loss and the gradient in dW. If you are not careful     #
  # here, it is easy to run into numeric instability. Don't forget the        #
  # regularization!                                                           #
  #############################################################################
  num_train = X.shape[0]
  scores = np.dot(X, W)
  scores = np.exp(scores) # 取指数
#   scores_sum = np.sum(scores, axis=1, keepdims=True)
  scores_sum = np.sum(scores, axis=1).reshape(-1,1)
  scores /= scores_sum
  loss = scores[np.arange(num_train), y]
  loss = -np.log(loss).sum()
  loss /= num_train
  loss += reg * np.sum(W*W)
  
  ###
  ds = scores
  ds[np.arange(num_train),y] = -(1-scores[np.arange(num_train),y])
  dW = np.dot(X.T, ds)
  dW /= num_train
  dW += 2 * reg * W












  #############################################################################
  #                          END OF YOUR CODE                                 #
  #############################################################################

  return loss, dW

