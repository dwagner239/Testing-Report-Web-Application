# Testing Report Web Application
Index and subtest scoring for the Repeatable Battery for the Assessment of Neuropsychological Status (RBANS)

The RBANS is a brief (less than 30 minutes), individually administered test that helps determine the neuropsychological status of adults ages 20 through 89 who have neurologic injury or disease such as dementia, head injury, and stroke. It assesses learning and memory, visual perception and construction, language, attention and processing speed. We use this measure on a daily basis in our outpatient clinic. Scoring requires that the professional look up values in a series of tables. In our use, reporting scores was done immediately after the patient was assessed and scores were reviewed by the neuropsychologist prior to meeting the patient on the same day, sometimes right after testing. So it was important to be able to do this very quickly and to minimize error -- best done by avoiding having to use tables to score.

I originally created an Excel workbook to aid in quick reporting of this instrument (as well as others). This code was the foundation of a web-based version and presented as a proof of concept for development of a web-based scoring and reporting platform. Ideally, the project would've been developed to provide a printed report and store scores in a database. The project was met with a lack of interest by management and I eventually took down the server instance and shelved the project. 

To be fully operational, the code requires a number of text files which contain the normative data for the test. I did not include these as the normative data is  copyrighted by the test publisher, Pearson. These would be used to derive the index scores by taking the subtest scores that comprise the index score up by locating the raw score of one subtest on the X axis of the table and the other on the Y axis and locating the resulting score at their intersection. Text files for the index scores would have followed the conventions in the table below and would've covered the following age ranges: 20-39, and then each decade afterward from 40-49 until 80-89.

<p align = "center">
  <img src= "https://github.com/dwagner239/RBANS_report/blob/main/table.png? raw=true">
</p>

Subtest scores were calculated from subtest means and standard deviations from a white paper released by Pearson around 2009. I first calculate the z-score by subtracting the patient's raw score from the sample mean and dividing that by the standard deviation. T-scores are rendered by multiplying the z-score by 10 and adding 50 (T-scores are a standardized metric with a mean of 50 and a standard deviation of 10) and rounding to a whole number. The text file containing the subtest scores is also not included due to copyright issues. The white paper has since been removed from the Pearson website, and subtest scoring incorporated into the newest version of the test released in 2012.

RBANS website: https://www.pearsonassessments.com/store/usassessments/en/Store/Professional-Assessments/Cognition-%26-Neuro/Repeatable-Battery-for-the-Assessment-of-Neuropsychological-Status-Update/p/100000726.html 
