import argparse

ap = argparse.ArgmentParser(description='database queries.')
ap.add_argument('-QN','--QuestionNumber',choices={'1', '2','3','4','5','6','7','8'})
ap.add_argument('-EI','--ExtraInformation')

#args_ = ap.parse_args()
args = vars(ap.parse_args())
