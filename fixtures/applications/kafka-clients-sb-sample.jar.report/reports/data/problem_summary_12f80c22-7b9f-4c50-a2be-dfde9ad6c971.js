MIGRATION_ISSUES_DETAILS["12f80c22-7b9f-4c50-a2be-dfde9ad6c971"] = [
{description: "<p>Remove the SpringBoot @SpringBootApplication annotation.<\/p><p>A Spring Boot application contains a \"main\" class with the @SpringBootApplication annotation. A Quarkus application does not have such a class. Two different alternatives can be followed - either to remove the \"main\" class associated with the annotation, or add the <code>org.springframework.boot:spring-boot-autoconfigure<\/code> dependency as an <code>optional<\/code> Maven dependency. An optional dependency is available when an application compiles but is not packaged with the application at runtime. Doing this would allow the application to compile without modification, but you would also need to maintain a Spring version along with the Quarkus application.<\/p>", ruleID: "springboot-annotations-to-quarkus-00000", issueName: "Remove the SpringBoot @SpringBootApplication annotation",
problemSummaryID: "12f80c22-7b9f-4c50-a2be-dfde9ad6c971", files: [
{l:"<a class='' href='Application_java.html?project=4423800'>com.rmarting.kafka.Application<\/a>", oc:"1"},
], resourceLinks: [
]},
];
onProblemSummaryLoaded("12f80c22-7b9f-4c50-a2be-dfde9ad6c971");