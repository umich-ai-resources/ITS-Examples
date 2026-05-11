# U-M Maizey API - Create an API Key

Once you’ve created your Maizey project and added an app to it, you’ll have access to the **Configure App** settings. Under Apps, click the three dots on the right side of the app name to access the **Configure App** settings.

![Getting Started](../docs/img/1configure_app.png)

To create a new API token, select **API Config** from the menu. Provide a purpose for the token, agree to the terms and conditions, and then click **Submit**. A pop-up window displays with your token. **Save it in a secure location; you will not be able to see it again after you close the popup.**


The **API Config** tab then displays an overview of all the events using that token. Click the **Documentation** button for information about how to use your token.

![Getting Started](../docs/img/2project_token.png)

# Navigating the U-M Maizey API Documentation

After opening your project, click the **API Config** tab, and then click the **Documentation** button.

![Getting Started](../docs/img/3documentation.png)

The following page displays, detailing Maizey’s API schema and allowing developers to try it out. To begin, click **Authorize** and paste your token in. Then, open the first collapsible panel. This endpoint allows you to create a MaizeyConversation.

![Getting Started](../docs/img/4authorize.png)
![Getting Started](../docs/img/5maizey_conversation.png)

Click **Try it out**, then navigate to the **Details** page for your Maizey project and copy the **Project ID**. Paste your ID into the **project_pk** field in the documentation. Finally, scroll down and click **Execute**. 

![Getting Started](../docs/img/6project_pk.png)

In the response, copy the number next to **“pk”**: (**1552** in the example pictured below). 

![Getting Started](../docs/img/7pk_value.png)

Open the second collapsible and click **Try it out**. Paste your **pk** into **conversation_pk** (it should be the integer from earlier). Then, paste your **Project ID** from earlier into **project_pk**. In the **Request body**, replace **“string”** with your query. Scroll down and click **Execute**. It may take a moment to load.

![Getting Started](../docs/img/8maizey_query.png)

The output will contain Maizey’s response.

![Getting Started](../docs/img/9maizey_response.png)

If you go back to your Maizey project, you will see that your query and response will also be reflected as a new chat. Remember that there is no endpoint for managing or deleting conversations or messages.

![Getting Started](../docs/img/10maizey_interface.png)