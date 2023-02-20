MIGRATION_ISSUES_DETAILS["613b43be-bf1d-4d47-9289-bf3d5c78335d"] = [
{description: "<p>Check if there is a Quarkus Extensions with Spring API compatibility for the Spring <code>spring-boot-loader<\/code> component.<br/> If yes, then replace the <code>org.springframework.boot:spring-boot-loader<\/code> dependency with the Quarkus extension.<br/> If no, consider rewrite the code that relies on this dependency leveraging the Quarkus Guides linked below.<\/p>", ruleID: "springboot-generic-catchall-groovy-00000", issueName: "Spring component spring-boot-loader requires investigation",
problemSummaryID: "613b43be-bf1d-4d47-9289-bf3d5c78335d", files: [
{l:"<a class='' href='pom_xml.41.html?project=4423800'>META-INF/maven/org.webjars/webjars-locator-core/pom.xml<\/a>", oc:"1"},
], resourceLinks: [
{h:"https://quarkus.io/guides/", t:"Quarkus - Guides"},
]},
];
onProblemSummaryLoaded("613b43be-bf1d-4d47-9289-bf3d5c78335d");