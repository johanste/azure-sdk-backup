We expect all Azure client libraries to go through rigorous APIs reviews similar to those conducted for all .NET APIs.
It's critical that the review is conducted early enough to allow time for fixes,
and sometimes significant API redesign based on the review feedback.
If you have never participated in an Azure client library API review,
we recommend that you schedule a pre-review (consulting session) before you start working on the APIs.

Note: Azure client library reviews are not REST API (nor swagger) reviews. We review language-specific client library APIs.
In particular, we review .NET, Python, Java, and JavaScript APIs, and in rare cases C/C++, Go, and other language client library.

## How to Design Great Azure APIs

Make sure your client libraries follow [Azure SDK Design Guidelines](https://github.com/Azure/azure-sdk/blob/master/docs/design/README.md).

## What to Prepare for a Review

To conduct a review, we need the following things from the owners of the client library:

1. Several code samples showing how the client library is meant to be used by customers. An example of a good set of usage samples can be found [here](https://github.com/dotnet/corefx/issues/32588).
2. A listing of 3-5 champion scenarios relevant to the developer. These must identify the critical scenarios that the majority of developers will experience. For each champion scenario, a link to a code sample in the repo must be provided. It is expected that these champion scenarios are optimized for, ensuring succinct, intuitive, and productive developer experiences are possible for each.
3. Link to the service documentation/specification.
4. Link to the service REST APIs, if applicable/available.
5. Listing of the APIs. See below for example and tools to generate it.
6. If the client library is already prototyped, dlls/packages/etc with the prototype implementation.
7. If the client library already GAed in the past, and this review is for additional APIs, old dlls/packages (to help us understand the changes).

## API Listings

During API reviews, we look at API usage samples (as discussed above) and at detailed API lisiting.
You can see an example of such listing [here](https://github.com/Azure/azure-sdk/blob/master/docs/design/dotnet/APIListingExample.md).

If you have a prototype of your APIs, depending on the language the APIs are for, you can possibly generate the API listing.

- If the API is a .NET APIs, use API Reviewer Tool at file://///fxcore//tools//docs//ApiReviewer.html
- If the API is a Python API, use reference documentation generated by Sphinx.
- If the API is a JavaScript/TypeScript API, provide the `d.ts` file for your client library. Use [API-Extractor](https://github.com/Microsoft/web-build-tools/wiki/API-Extractor) to produce a single file with your entire API surface area. Note that API-Extractor does not need to complete without error in order to produce the rollup `d.ts` file.
- If the API is a Java API, use your preferred build tool to generate a JavaDoc output (e.g. `mvn javadoc:javadoc` with Maven), and zip up the output.
- For all other languages, send email to kcwalina to discuss the best format on individual basis.

If you don't have a prototype, you surely have the design spec on paper :-)

## API Review Lifecycle
1. The team submitting APIs for review files a git hub issue (this repo). The issue should link to all documents discussed above.
2. The review team will schedule one or more review sessions (depending on the size of the API).
3. After reviews are completed, the review team will publish a report with recommendations.

## See Also

1. [CoreFx API Review Process](https://github.com/dotnet/corefx/blob/master/Documentation/project-docs/api-review-process.md)
