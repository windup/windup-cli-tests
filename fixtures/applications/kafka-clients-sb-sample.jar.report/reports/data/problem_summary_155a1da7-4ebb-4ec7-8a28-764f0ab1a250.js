MIGRATION_ISSUES_DETAILS["155a1da7-4ebb-4ec7-8a28-764f0ab1a250"] = [
{description: "<p>Check if there is a Quarkus Extensions with Spring API compatibility for the Spring <code>spring-beans<\/code> component.<br/> If yes, then replace the <code>org.springframework:spring-beans<\/code> dependency with the Quarkus extension.<br/> If no, consider rewrite the code that relies on this dependency leveraging the Quarkus Guides linked below.<\/p>", ruleID: "springboot-generic-catchall-groovy-00000", issueName: "Spring component spring-beans requires investigation",
problemSummaryID: "155a1da7-4ebb-4ec7-8a28-764f0ab1a250", files: [
{l:"<a class='' href='pom_xml.107.html?project=4423800'>META-INF/maven/org.yaml/snakeyaml/pom.xml<\/a>", oc:"1"},
], resourceLinks: [
{h:"https://quarkus.io/guides/", t:"Quarkus - Guides"},
]},
];
onProblemSummaryLoaded("155a1da7-4ebb-4ec7-8a28-764f0ab1a250");