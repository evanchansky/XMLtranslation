<?xml version="1.0" encoding="UTF-8" standalone="no" ?>
<xsd:schema xmlns:xsd="http://www.w3.org/2001/XMLSchema">
	<xsd:element name="resources">
		<xsd:complexType>
			<xsd:sequence>
				<xsd:element name="string" maxOccurs="unbounded">
					<xsd:complexType>
						<xsd:simpleContent>
							<xsd:extension base="xsd:string">
								<xsd:attribute name="name" type="xsd:string"/>
							</xsd:extension>
						</xsd:simpleContent>
					</xsd:complexType>
				</xsd:element>
			</xsd:sequence>
		</xsd:complexType>
	</xsd:element>
</xsd:schema>
