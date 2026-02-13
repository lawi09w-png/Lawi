import pandas as pd

class WeeklyReportGenerator:
    def __init__(self, data_file):
        self.data_file = data_file

    def generate_report(self):
        # Load data
        data = pd.read_csv(self.data_file)
        
        # Generate weekly report
        report = data.groupby('Category').size().reset_index(name='Counts')
        
        # Save report to a new CSV file
        report.to_csv('weekly_report.csv', index=False)
        print('Weekly report generated: weekly_report.csv')

if __name__ == '__main__':
    generator = WeeklyReportGenerator('sample_data.csv')
    generator.generate_report()