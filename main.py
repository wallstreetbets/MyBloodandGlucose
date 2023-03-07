import matplotlib.pyplot as plt
import pandas as pd


file_blood = "blood_data.csv"
file_glucose = "../../Documents/GitHub/MyBloodandGlucose/glucose.csv"


def glucose_display(frame):
	frame.boxplot()
	frame.plot()
	plt.show()


def blood_display(frame):
	frame.boxplot()
	plt.style.use('dark_background')
	frame.hist()
	frame.plot()
	plt.show()


def blood(episode, plot=False):
	"""
	:param episode: 'None' will return all data, 'True' only when episodes happened, 'False' when it didn't.
	:param plot: 'True' will plot boxplot, hist, plot; 'False' will not display at all
	:return: DataFrame
	"""
	df_blood = pd.read_csv(file_blood, index_col='Date', parse_dates=True)
	if episode:
		df_blood = df_blood.loc[(df_blood['Episode'])]
		if plot:
			del df_blood['Episode']
			blood_display(df_blood)
			plt.show()
	elif not episode:
		df_blood = df_blood.loc[(df_blood['Episode'] == False)]
		del df_blood['Intensity']
		if plot:
			del df_blood['Episode']
			blood_display(df_blood)
			plt.show()
	else:
		del df_blood['Intensity']
		if plot:
			del df_blood['Episode']
			blood_display(df_blood)
			plt.show()
	return df_blood


def glucose(fasting=False, episode=False, plot=False):
	"""
	:param fasting: 'True' only when you wake up and havent eaten, 'False' when the opposite.
	:param episode: 'None' will return all data, 'True' only when episodes happened, 'False' when it didn't.
	:param plot: 'True' will plot boxplot, hist, plot; 'False' will not display at all
	:return: DataFrame
	"""
	df_glucose = pd.read_csv(file_glucose, index_col='Date', parse_dates=True)
	if fasting:
		df_glucose = df_glucose.loc[df_glucose['Fasting']]
		if plot:
			glucose_display(df_glucose)
			plt.show()
	elif not fasting:
		df_glucose = df_glucose.loc[df_glucose['Fasting'] == False]
		if plot:
			glucose_display(df_glucose)
			plt.show()
	elif episode:
		df_glucose = df_glucose.loc[df_glucose['episode']]
		if plot:
			glucose_display(df_glucose)
			plt.show()
	elif not episode:
		df_glucose = df_glucose.loc[df_glucose['episode'] == False]
		if plot:
			glucose_display(df_glucose)
			plt.show()

	return df_glucose


if __name__ == '__main__':
	# print(glucose(fasting=True))
	print(blood(episode=True, plot=True))
	# print(blood(episode=None, plot=True))
	# print(blood(episode=False, plot=True))


