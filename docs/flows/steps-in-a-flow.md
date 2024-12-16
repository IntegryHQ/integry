---
icon: stairs
---

# Steps in a Flow

## HTTP Call <a href="#h_01hs98kaqg1m42c0azwjv3wxja" id="h_01hs98kaqg1m42c0azwjv3wxja"></a>

Add the HTTP call step to a trigger block to make a call to an API endpoint of any app that Integry supports, including yours.

Note: If your app does not have a public API, please review our [recommendations](https://docs.integry.io/hc/en-us/articles/22983863682969) before you build it. Alternatively, you could also just connect directly to your database!

## Action in an app <a href="#h_01hs98k8ag94nrsnxt8k49vqmz" id="h_01hs98k8ag94nrsnxt8k49vqmz"></a>

Integry supports [200+ apps](https://www.integry.ai/apps). You can add a query or an action of those apps as a step in a flow block.

In order to run those queries or actions, we will get your user to login to the app (hence, "using _user's_ auth"), and configure any fields that require their input. You can pre-configure some parts of it.

Alternatively, you can also perform an action in another app using _your_ auth. In that case, you will login and configure the step.

A trigger block can include both types of actions.

### Action in an app with your account <a href="#h_01hs9ac83hgzxgs5ct3z66e9mr" id="h_01hs9ac83hgzxgs5ct3z66e9mr"></a>

Typically, you would perform an action in another app using user's auth as a step in a flow block. However, that action will be executed using your user's account of that app. What if you want to use your _own_ account?

Let's consider an example:

<figure><img src="../.gitbook/assets/image (19).png" alt="" width="375"><figcaption></figcaption></figure>

When an Account is Created in Salesforce, you make an HTTP call to your app (with the account details) to add a new contact. You also then send an email notification to the user informing them that a new account just got synced.

* Accounts are accessed from Salesforce using the user's auth.
* The HTTP call is made to your app using an API key of your app.
* The email notification is sent using the Send New Email action in the Mailchimp Transactional app using _your_ auth. You obviously want to send notifications to your users from _your_ account. &#x20;

<figure><img src="../.gitbook/assets/image (20).png" alt="" width="375"><figcaption></figcaption></figure>

## Custom code <a href="#h_01hs98k631ff8y3kjszcs6va1m" id="h_01hs98k631ff8y3kjszcs6va1m"></a>

Sometimes when building your flows, you need to add custom logic, formatting or processing. You can do all of this using Custom Code.&#x20;

You can add custom code at any point in your flow. The code step supports Python 3.12 with additional languages planned.&#x20;

<figure><img src="../.gitbook/assets/image (10).png" alt=""><figcaption></figcaption></figure>

1. Your code must be enclosed in a main() function&#x20;
2. You have access to the global steps dictionary of all the steps in the flow including their in variables and out variables
3. Anything you return becomes available in the flow in the code steps's out variable
4. You can return any data type and it will be made available: strings, numbers, dictionaries, arrays etc
5. You can also create functions and use them in your code&#x20;

### Writing and Testing Code <a href="#h_01hqdszy11ddym65r18dcxy3pd" id="h_01hqdszy11ddym65r18dcxy3pd"></a>

Here's sample code that returns a full name by concatenating first name and last name with a space

```
def main():
  return steps.salesforce_contact_created.out.first_name + ' ' + steps.salesforce_contact_created.out.last_name
```

You can see that we're referring to steps global dictionary to access salesforce\_contact\_created trigger's first\_name and last\_name.&#x20;

You can insert fields using the insert field menu&#x20;

<figure><img src="../.gitbook/assets/image (11).png" alt=""><figcaption></figcaption></figure>

Once you have your code written out, you can test it by hitting the, you guessed it, the Test button. You'll see the exact output below. The structure of the output is important since it will be made available in the field insert menu for any subsequent step.

Here's the output of code we tested:

<figure><img src="../.gitbook/assets/image (12).png" alt=""><figcaption></figcaption></figure>

In the subsequent steps, the field insert menu for the code step has:

<figure><img src="../.gitbook/assets/image (13).png" alt="" width="312"><figcaption></figcaption></figure>

### Outputting Different Data Types <a href="#h_01hqdwfste8a4jnbhrjk7w1mb9" id="h_01hqdwfste8a4jnbhrjk7w1mb9"></a>

If you return a dictionary, it will be available as-is in the output:

<figure><img src="../.gitbook/assets/image (14).png" alt=""><figcaption></figcaption></figure>

Here's the field insert menu:

<figure><img src="../.gitbook/assets/image (15).png" alt="" width="289"><figcaption></figcaption></figure>

You can also output arrays and more complex nested dictionaries

#### Importing Modules <a href="#h_01hqr39knq3zfek5wep4nkrh5w" id="h_01hqr39knq3zfek5wep4nkrh5w"></a>

You can import Python modules as well. We support any [standard modules](https://docs.python.org/3/library/index.html), as well as lxml, bs4, and pytz

You can mention the module you want to import at the top

```python
import re

def main():
  txt = "The rain in Spain"
  return re.search("^The.*Spain$", txt)
```

## IF condition <a href="#h_01hs98k3kj1q07x10ympzpc6m1" id="h_01hs98k3kj1q07x10ympzpc6m1"></a>

The IF condition step allows you to add branching logic to a trigger block.

The conditions are evaluated at run-time and the steps in the appropriate group -- IF, ELSE IF, ELSE -- are executed.&#x20;

For instance, if the value of a "Type" field in the trigger payload from another app equals "Created", run the Create action in Acme. Otherwise, run the Update action in Acme.

<figure><img src="../.gitbook/assets/image (16).png" alt="" width="375"><figcaption></figcaption></figure>

### IF

An IF condition can have one or more condition statements that each have three parts: data, operator and value. These statements can chained with an AND or OR operator.

For instance, this checks if the "type" field value is "Created" or "created".

<figure><img src="../.gitbook/assets/image (17).png" alt=""><figcaption></figcaption></figure>

The steps in the IF condition group will run if, at run-time, the entire expression is true.

### ELSE IF <a href="#h_01hqrzt31n19vz0c5cm8ar85vm" id="h_01hqrzt31n19vz0c5cm8ar85vm"></a>

If you want to add more branching logic to the IF condition, you can add one or more ELSE IF steps from the Add Step menu. Each ELSE IF will have it's own condition statements, and steps to run if the condition statements are true at run-time.

### ELSE <a href="#h_01hqrzsz0q6xp558cty8qrcynt" id="h_01hqrzsz0q6xp558cty8qrcynt"></a>

Finally, you can also add an ELSE branch to the IF condition that will execute if the IF condition, and all it's ELSE IFs (if you've added any), fail, i.e., their condition statements result in false.

### Condition statement <a href="#h_01hqs04d1e9pz5q6c0gr47d2hc" id="h_01hqs04d1e9pz5q6c0gr47d2hc"></a>

A condition statement has three parts: data, [operator](steps-in-a-flow.md#h_01hqrw72nn97xbv1bb8sx67q9h), and value.

Typically, data (left-hand side) will be a field, possibly from the output of a previous step, the value (right-hand side) will be a static value (but can be a field's value at runtime as well), and the operator will specify how to compare the two sides. Some operators, like is empty or is true, already include the respective values so you don't have to specify them.

Integry supports conditional statements in two types of steps: IF condition, and Do While Loop.

#### Data types <a href="#h_01hs98jbtaw0v87a2bk09nzr8s" id="h_01hs98jbtaw0v87a2bk09nzr8s"></a>

When using the Conditions, you don't have to specify data type, Integry will make best effort to coerce the type and use the appropriate comparison. When entering strings, you do not need to enclose them in quotes, the same is true for numbers. In addition, comparison is case sensitive for strings.

### Operators <a href="#h_01hqrw72nn97xbv1bb8sx67q9h" id="h_01hqrw72nn97xbv1bb8sx67q9h"></a>

#### **equals**

This operator checks if left hand side is equal to right hand side.

#### **does not equal**

This operator is a negation of "equals", and will evaluate to true for all cases where "equals" evaluates to false, and false otherwise.

#### **is true**

This operator checks if given value is true. If the value is not a boolean, following rules are used to evaluate the condition.

1. If value is an array, the operator evaluates to true if array is empty, false otherwise.
2. If value is an object, the operator evaluates to true if object has at least one key, false otherwise.
3. If value is a string, the operator evaluates to true if string is not empty and not false or null, false otherwise.
4. If value is a number, the operator evaluates to true if number is not 0, false otherwise.

#### **is not true**

This operator is a negation of "is true", and will evaluate to true for all cases where "is true" evaluates to false, and false otherwise.

#### **contains**

This operator checks if right hand side is part of left hand side. The following rules are used to evaluate the condition:

1. If left hand side is a string, the operator evaluates to true if right hand side is present in the string, false otherwise.
2. If left hand side is an array, the operator evaluates to true if right hand side is present in the array, false otherwise.
3. If left hand side is an object, the operator evaluates to true if right hand side is present in the object as a value, false otherwise.
4. If left hand side is a boolean, number or null, it is coerced to a string and operator is applied on the string value.

#### **does not contain**

This operator is a negation of "contains", and will evaluate to true for all cases where "contains" evaluates to false, and false otherwise. Similar to **contains**, you can use strings, arrays or objects.

#### **starts with**

This operator checks if elements at the start of left hand side are equal to right hand side.

1. If left hand side is not a string, following rules are used to evaluate the condition.
2. If left hand side is a string, the operator evaluates to true if the right hand side is the start of the string, false otherwise.
3. If left hand side is an array, the operator evaluates to true if the right hand side is the first element of the array, false otherwise.
4. If left hand side is an object, the operator evaluates to false.

#### **does not start with**

This operator is a negation of "starts with", and will evaluate to true for all cases where "starts with" evaluates to false, and false otherwise.

#### **ends with**

This operator checks if elements at the end of left hand side are equal to right hand side. If left hand side is not a string, following rules are used to evaluate the condition.

1. If left hand side is an array, the operator evaluates to true if the right hand side is the last element of the array, false otherwise.
2. If left hand side is an object, the operator evaluates to false.

#### **greater than**

This operator checks if left hand side is greater than right hand side. If either side is not a number, following rules are used to evaluate the condition.

1. If either side is a string, a lexicographical comparison is performed.
2. If either side is a boolean or null, it is coerced to a string and a lexicographical comparison is performed.
3. If either side is an array, the operator is applied on each element using "AND" logical relation.
4. If either side is an object, the operator is applied on each key and value using "AND" logical relation.

#### **less than**

This operator checks if left hand side is less than right hand side. If either side is not a number, following rules are used to evaluate the condition.

1. If either side is a string, a lexicographical comparison is performed.
2. If either side is a boolean or null, it is coerced to a string and a lexicographical comparison is performed.
3. If either side is an array, the operator is applied on each element using "AND" logical relation.
4. If either side is an object, the operator is applied on each key and value using "AND" logical relation.

#### **is empty**

This operator checks if value is an empty string. If value is not a string, following rules are used to evaluate the condition.

1. If value is an array, the operator evaluates to true if array is empty, false otherwise.
2. If value is an object, the operator evaluates to true if object has no keys, false otherwise.
3. If value is a boolean, number or null, the operator evaluates to false.

#### **is not empty**

This operator is a negation of "is empty", and will evaluate to true for all cases where "is empty" evaluates to false, and false otherwise.

## Abort <a href="#h_01hs9953qfnqcmtw9trb5zg9ek" id="h_01hs9953qfnqcmtw9trb5zg9ek"></a>

Add an abort step to a flow block to abort the execution of a run. This is used when you want to explicitly handle execution errors (and don't want Integry to kill the run).

## Wait <a href="#h_01hs9987dkg9wzpjkdc0pf9ba5" id="h_01hs9987dkg9wzpjkdc0pf9ba5"></a>

Add a wait step to a flow block to pause the execution of a run for a set period.

## Do While Loop <a href="#h_01hs99zrd2n6x6fp0a91qqh59k" id="h_01hs99zrd2n6x6fp0a91qqh59k"></a>

A Do While Loop allows you to execute a group of steps in a trigger block, and then either repeat the group or exit the loop depending on one or more condition statements.

For instance, get all records by making repeated [HTTP Calls](steps-in-a-flow.md#h_01hs98kaqg1m42c0azwjv3wxja) to an endpoint that returns 100 records per page, until there are no more records available, loop over the records in a page (using a For Loop), and create customers in Acme.

<figure><img src="../.gitbook/assets/image (18).png" alt="" width="375"><figcaption></figcaption></figure>

### Do <a href="#h_01hs99ym4a2ybvznh89zrbwzad" id="h_01hs99ym4a2ybvznh89zrbwzad"></a>

Add the steps you want to repeat to the Do step group.

### While <a href="#h_01hqtpdb9vvsx6bwnn621a3a71" id="h_01hqtpdb9vvsx6bwnn621a3a71"></a>

The loop will continue to repeat while the condition is true. The condition is specified as one or more [condition statements](steps-in-a-flow.md#h_01hs98k3kj1q07x10ympzpc6m1) that each have three parts: data, operator, and value. These statements can be chained with an OR or AND operator.
