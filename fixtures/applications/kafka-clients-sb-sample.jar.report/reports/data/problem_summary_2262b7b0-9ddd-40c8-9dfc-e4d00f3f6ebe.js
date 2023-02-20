MIGRATION_ISSUES_DETAILS["2262b7b0-9ddd-40c8-9dfc-e4d00f3f6ebe"] = [
{description: "<p>Check if there is a Quarkus Extensions with Spring API compatibility for the Spring <code>spring-context-support<\/code> component.<br/> If yes, then replace the <code>org.springframework:spring-context-support<\/code> dependency with the Quarkus extension.<br/> If no, consider rewrite the code that relies on this dependency leveraging the Quarkus Guides linked below.<\/p>", ruleID: "springboot-generic-catchall-groovy-00000", issueName: "Spring component spring-context-support requires investigation",
problemSummaryID: "2262b7b0-9ddd-40c8-9dfc-e4d00f3f6ebe", files: [
{l:"<a class='' href='pom_xml.107.html?project=4423800'>META-INF/maven/org.yaml/snakeyaml/pom.xml<\/a>", oc:"1"},
], resourceLinks: [
{h:"https://quarkus.io/guides/", t:"Quarkus - Guides"},
]},
];
onProblemSummaryLoaded("2262b7b0-9ddd-40c8-9dfc-e4d00f3f6ebe");