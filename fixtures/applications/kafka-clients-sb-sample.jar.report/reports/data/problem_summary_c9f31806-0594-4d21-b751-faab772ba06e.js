MIGRATION_ISSUES_DETAILS["c9f31806-0594-4d21-b751-faab772ba06e"] = [
{description: "<p>Replace <code>springdoc.swagger-ui.path<\/code> with <code>quarkus.swagger-ui.path<\/code><\/p><p>By adding <code>quarkus.swagger-ui.always-include=true<\/code> Quarkus will always expose the Swagger UI endpoint. It is only exposed in Dev mode by default.<\/p>", ruleID: "springboot-properties-to-quarkus-00005", issueName: "Replace Spring Swagger endpoint mapping",
problemSummaryID: "c9f31806-0594-4d21-b751-faab772ba06e", files: [
{l:"<a class='' href='application_properties.html?project=4423800'>BOOT-INF/classes/application.properties<\/a>", oc:"1"},
], resourceLinks: [
{h:"https://quarkus.io/guides/openapi-swaggerui", t:"Quarkus Guide - using OpenAPI and Swagger"},
]},
];
onProblemSummaryLoaded("c9f31806-0594-4d21-b751-faab772ba06e");