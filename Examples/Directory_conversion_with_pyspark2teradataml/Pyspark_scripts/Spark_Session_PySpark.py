# Disclaimer
# The sample code ("Sample Code") provided is not covered by any Teradata agreements. 
# Please be aware that Teradata has no control over the model responses to such sample 
# code and such response may vary. The use of the model by Teradata is strictly for 
# demonstration purposes and does not constitute any form of certification or endorsement. 
# The sample code is provided "AS IS" and any express or implied warranties, including the 
# implied warranties of merchantability and fitness for a particular purpose, are disclaimed. 
# In no event shall Teradata be liable for any direct, indirect, incidental, special, exemplary, 
# or consequential damages (including, but not limited to, procurement of substitute goods or services; 
# loss of use, data, or profits; or business interruption) sustained by you or a third party, 
# however caused and on any theory of liability, whether in contract, strict liability, or tort 
# arising in any way out of the use of this sample code, even if advised of the possibility of such damage.

from pyspark.sql import SparkSession
spark_session = SparkSession.builder.
                getOrCreate()