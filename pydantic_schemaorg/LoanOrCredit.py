from __future__ import annotations
from typing import TYPE_CHECKING

from pydantic import AnyUrl, StrictBool, StrictInt, StrictFloat
from typing import List, Optional, Union


from pydantic import Field
from pydantic_schemaorg.FinancialProduct import FinancialProduct


class LoanOrCredit(FinancialProduct):
    """A financial product for the loaning of an amount of money, or line of credit, under agreed"
     "terms and charges.

    See: https://schema.org/LoanOrCredit
    Model depth: 5
    """
    type_: str = Field(default="LoanOrCredit", alias='@type', const=True)
    renegotiableLoan: Optional[Union[List[Union[StrictBool, 'Boolean', str]], StrictBool, 'Boolean', str]] = Field(
        default=None,
        description="Whether the terms for payment of interest can be renegotiated during the life of the loan.",
    )
    currency: Optional[Union[List[Union[str, 'Text']], str, 'Text']] = Field(
        default=None,
        description="The currency in which the monetary amount is expressed. Use standard formats: [ISO 4217"
     "currency format](http://en.wikipedia.org/wiki/ISO_4217), e.g. \"USD\"; [Ticker"
     "symbol](https://en.wikipedia.org/wiki/List_of_cryptocurrencies) for cryptocurrencies,"
     "e.g. \"BTC\"; well known names for [Local Exchange Trading Systems](https://en.wikipedia.org/wiki/Local_exchange_trading_system)"
     "(LETS) and other currency types, e.g. \"Ithaca HOUR\".",
    )
    requiredCollateral: Optional[Union[List[Union[str, 'Text', 'Thing']], str, 'Text', 'Thing']] = Field(
        default=None,
        description="Assets required to secure loan or credit repayments. It may take form of third party pledge,"
     "goods, financial instruments (cash, securities, etc.)",
    )
    loanTerm: Optional[Union[List[Union['QuantitativeValue', str]], 'QuantitativeValue', str]] = Field(
        default=None,
        description="The duration of the loan or credit agreement.",
    )
    loanType: Optional[Union[List[Union[AnyUrl, 'URL', str, 'Text']], AnyUrl, 'URL', str, 'Text']] = Field(
        default=None,
        description="The type of a loan or credit.",
    )
    recourseLoan: Optional[Union[List[Union[StrictBool, 'Boolean', str]], StrictBool, 'Boolean', str]] = Field(
        default=None,
        description="The only way you get the money back in the event of default is the security. Recourse is"
     "where you still have the opportunity to go back to the borrower for the rest of the money.",
    )
    gracePeriod: Optional[Union[List[Union['Duration', str]], 'Duration', str]] = Field(
        default=None,
        description="The period of time after any due date that the borrower has to fulfil its obligations before"
     "a default (failure to pay) is deemed to have occurred.",
    )
    loanRepaymentForm: Optional[Union[List[Union['RepaymentSpecification', str]], 'RepaymentSpecification', str]] = Field(
        default=None,
        description="A form of paying back money previously borrowed from a lender. Repayment usually takes"
     "the form of periodic payments that normally include part principal plus interest in"
     "each payment.",
    )
    amount: Optional[Union[List[Union[StrictInt, StrictFloat, 'Number', 'MonetaryAmount', str]], StrictInt, StrictFloat, 'Number', 'MonetaryAmount', str]] = Field(
        default=None,
        description="The amount of money.",
    )
    

if TYPE_CHECKING:
    from pydantic_schemaorg.Boolean import Boolean
    from pydantic_schemaorg.Text import Text
    from pydantic_schemaorg.Thing import Thing
    from pydantic_schemaorg.QuantitativeValue import QuantitativeValue
    from pydantic_schemaorg.URL import URL
    from pydantic_schemaorg.Duration import Duration
    from pydantic_schemaorg.RepaymentSpecification import RepaymentSpecification
    from pydantic_schemaorg.Number import Number
    from pydantic_schemaorg.MonetaryAmount import MonetaryAmount
