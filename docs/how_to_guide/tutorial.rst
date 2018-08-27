

Using the Tagging Tool
======================

This section will walk through the steps for using the tagging tool
application.

Start the Application
---------------------

1. Open a terminal window 

:Linux:      ``Ctrl`` + ``Alt`` + ``T``
:Windows:    ``Windows`` + ``R`` -> Type 'cmd'
:Mac:        ``⌘`` + ``Space`` -> Type 'Terminal'


2. Launch the app by typing in ``nestor-gui``

3. The application should open as seen below:

|image6|

4. Open your .csv file with your MWOs. Included in the application, is a
   publicly available dataset. We will use this file (excavators.csv) as
   the example.

|image7|

|image8|

5. If you are using the application for the first time, hit “Next”

|image9|

  If you are continuing from a previous session of tagging using Nestor,
  load up the 1-gram and the N-gram files. Usually, they are automatically
  loaded up using the same file-path as the .csv file. If the file-path has
  changed, ensure that the correct 1-gram and N-gram files are selected using
  the **Open** button.

|image91|

6. Select the column(s) that you would like to “tag.” In this example,
   the column is “OriginalShorttext.”

|image10|

7. There is also a drop-down to say what the column likely represents -
   this is for later analyses and future storage in a graph database. These categories
   in the drop-down come from `prior studies<https://www.nist.gov/publications/developing-maintenance-key-performance-indicators-maintenance-work-order-data>`__ on Maintenance Key Performance Indicators (KPIs).
   These categories are used as the headers in the *.h5* binary files used to store the tagged data (`See the Report section <#sec:Report>`__).
   A subset of these categories, *Machine Name* and *Maintenance Technician*, are used for the `Nestor Dashboard <dash-demonstration.rst>`__.

   These categories will be used for constructing a graph database (COMING SOON!)

   The “OriginalShorttext” in this example matches "Description of Problem". Hit “Next”.

|image101|

8. The application window will open as seen below:

|image11|


.. _sec:1gram:
1 Gram Token tab
----------------

This subsection will describe the features of the application and goes
into detail on the “1 Gram Token” tab.

|image12|

-  This window contains the following information:

   -  **tokens**: The token as seen in the corpus and ranked by `TF-IDF weighting <http://scikit-learn.org/stable/modules/feature_extraction.html#tfidf-term-weighting>`__.

   -  **NE**: This is a “Named Entity.” This column will track the
      classifications of the tokens, which will be explained in more
      detail later in the `Named Entity Classification Step <#sec:Classify>`__.

   -  **alias**: This column tracks any aliases for tokens as made by the
      tool. These represent your new “tags."

   -  **notes**: This column tracks your notes for any tokens you have
      mapped to an alias.


-  Next, select a token to “tag.” In this example, we use “replace.”


|image13|

-  The “similar pattern” field will display words similar to the token
   using an “edit-distance"-based metric, via `fuzzywuzzy <https://github.com/seatgeek/fuzzywuzzy>`__. Any term
   that is selected here will be given the same alias and classification
   as the original token. So in this example, if “replaced” is selected,
   it will be given the same alias, notes, and classification as
   “replace”

|image14|

-  The “alias” field will allow a user to enter any alias they would
   like for a token. The field will auto suggest the “token” as-is as
   the initial alias, but the user has the ability to change it to any
   alias they desire.

|image15|

.. _sec:Classify:

-  This field is where the user can classify the “token.” The
   classifications provided are:

   -  **Item**: The objects directly relevant to the issue such as
      machine, resources, parts, etc. An example is a “pump” is always
      an item, however, “pumping” would not be an item.

   -  **Problem**: The problem that is occurring at an item. An example is
      “leak” is always a problem.

   -  **Solution**: The solution action taken on an item. An example is
      “replace” is always a solution.

   -  **Ambiguous (Unknown)**: Words that are unknown without more
      context. An example is “oil” as this can be an item or a solution.
      This is further described in the `N Gram Token tab section <#sec:Ngram>`__

   -  **Stop-word**: A word that does not matter for analysis. For
      example, “see” or “according” are stop-words.

|image16|

-  The “Notes” field allows users to enter notes about the
   token/classifications.

|image17|

- For each new session, regardless of whether using earlier tagged 1-gram and
  N-gram files, each new word that is classified will be highlighted in a
  different color.

|image171|


.. _sec:Ngram:

N Gram Token tab
----------------

This subsection will describe the features of the application and goes
into detail on the “N Gram Token” tab.

-  The N Gram token tab will provide detail on common 2 grams tokens,
   ordered in TF-IDF ranking, for the corpus (e.g., “hydraulic leak” is
   a common 2 gram in some data sets). The 2 grams can also provide more
   context for the “Unknown” classifications from the above section. For
   example, “oil” is unknown until the user is provided more context.

|image18|

-  When a user selects the N Gram Token tab, the window below is
   presented. Initially all the n-gram Named Entity classes are empty.

|image19|

-  If the menu option for "Auto-populate" -> "From 1gram Vocab" is chosen,
   the user is then presented with the "Composition" of the 2 gram, which are
   composed of two 1 gram tokens.

|image191|
|image192|

-  Each 1 gram is presented, with the classification (“type”) and the
   synonyms (the other words that were linked with the Similar Pattern
   subwindow in the `1 Gram Token tab section <#sec:1gram>`__).
   In this example, “oil” is an “unknown (U)” classification and has no
   other synonyms at this point; “leak” is a “problem (P)” and has no
   other synonyms at this point.

|image20|

-  There are a number of classifications that a user can select for a 2
   grams. The user will have to classify any 2 grams that contain an “U”
   classification. Please note that some 2 grams will be pre-classified
   based on a ruleset as seen below:

|image21|

- **Problem Item**: This is a problem-item (or item-problem) pair. For example, “hydraulic” is an item and “leak” is a problem so “hydraulic leak” is a problem-item pair. The tool will pre-populate some problem-item pairs using the 1 grams that are classified as problems and items. The user will need to confirm these pairs are correct. 

-  **Solution Item**: This is a solution-item (or item-solution) pair. For example, “hydraulic” is an item and “replace” is a solution so “replace hydraulic” is a solution-item pair. The tool will pre-populate some solution-item pairs using the 1 grams that are classified as solutions and items. The user will need to confirm these pairs are correct. 

-  **Item**: This is for pairs of items that are de facto 1-grams. For example “grease” is an item, line is an “item”, but a “grease_line” is most likely its own “item". The tool will pre-populate some items based on 1 grams that are both items. The user will need to confirm these pairs are correct. Please note that 2 gram items, since they are really being treated as 1-grams, must have an underscore (_) in their alias, between the 2 individual items as seen below:

|image22|

-  **Problem**: This is a problem that is a 2 gram. This will be left up to the user to classify as these will not be pre-populated using 1 gram classifications. Please note that 2 gram problems, since they are  being treated as 1-grams, must have an underscore (_) in their alias, between the 2 individual problems.

-  **Solution**: This is a solution that is a 2 gram. This will be left up to the user to classify as these will not be pre-populated using 1 gram classifications. Please note that 2 gram solutions, since they are really being treated as 1-grams, must have an underscore (_) in their alias, between the 2 individual solutions.

-  **Ambigious (Unknown)**: This is an unknown 2 gram that needs more context. This will be left up to the user to classify as these will not be pre-populated using 1 gram classifications.

-  **Stop-word**: This is 2 gram stop-word. This will be pre-populated when a “solution” 1 gram is paired with a “problem” ‘ gram. The user can decide if any other 2 grams are not useful.


.. _sec:Report:
Report tab
----------------------------------

Once the user is done tagging their desired amount of tokens, they can
begin using the report tab.

-  Please make sure to hit the “update tag extraction” button before
   proceeding. This may take some time to compute. Please note on Windows computers, the application may state "Not Responding", however, the application is often still running. 

|image23|

-  The bottom graph will update. It explains the amount of tagging that
   has been completed. The distribution of documents (shown as a
   histogram) is calculated over the precision for each document (i.e.
   of the tokens found in a document, what fraction have a valid
   classification defined).

|image24|

-  Summary statistics are also shown: 

   -  **Tag PPV**: This is the Tag `Positive Predictive Value (PPV) <https://en.wikipedia.org/wiki/Positive_and_negative_predictive_values>`__.

   -  **Complete Docs**: This is the number of MWOs that have all of the tokens completely tagged. In this example, 178 MWOs are completely tagged out of a possible 5485, which is 3.25%.

   -  **Empty Docs**: This is the number of MWOs that have zero tokens tagged. In this example, 1738 MWOs have no tokens tagged out of a possible 5485, which is 31.69%.

|image25|

-  The “create new CSV” button will create an .csv with the original
   dataset and 7 new columns (“I”,“P”,”PI”, “S”,“SI”,“U”, and “X”) ,
   which contain the new tags from each category. Please note that “X”
   contains any stop words.

|image26|

-  The “create a HDFS (binary)” button will create a .h5 file. This file
   will be utilized later on to visualise the data on the Nestor Dashboard.
   It stores the tagged data with three keys - the original data ( **only columns with
   updated headers! ** ), an occurrence matrix for tags versus documents, and an
   occurrence matrix for Problem-Items - Solution-Items versus documents.

|image27|





.. |image6| image:: images/Graphics34_v3.png
.. |image7| image:: images/Graphics35_v3.png
.. |image8| image:: images/Graphics36_v3.png
.. |image9| image:: images/Graphics37_v3.png
.. |image91| image:: images/Graphics37_v3_2.png
.. |image10| image:: images/Graphics38_v3.png
.. |image101| image:: images/Graphics38_v3_2.png
.. |image11| image:: images/Graphics40_v3.png
.. |image12| image:: images/Graphics41_v3.png
.. |image13| image:: images/Graphics42_v3.png
.. |image14| image:: images/Graphics43_v3.png
.. |image15| image:: images/Graphics44_v3.png
.. |image16| image:: images/Graphics45_v3.png
.. |image17| image:: images/Graphics46_v3.png
.. |image171| image:: images/Graphics46_v3_2.png
.. |image18| image:: images/Graphics47_v3.png
.. |image19| image:: images/Graphics48_v3.png
.. |image191| image:: images/Graphics48_v3_2.png
.. |image192| image:: images/Graphics48_v3_3.png
.. |image20| image:: images/Graphics49_v3.png
.. |image21| image:: images/Graphics50_v3.png
.. |image22| image:: images/Graphics51_v3.png
.. |image23| image:: images/Graphics52_v3.png
.. |image24| image:: images/Graphics53_v3.png
.. |image25| image:: images/Graphics54_v3.png
.. |image26| image:: images/Graphics55_v3.png
.. |image27| image:: images/Graphics56_v3.png

