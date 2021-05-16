import { render } from '@testing-library/react';

import MarketingAppLandingPage from './marketing-app-landing-page';

describe('MarketingAppLandingPage', () => {
  it('should render successfully', () => {
    const { baseElement } = render(<MarketingAppLandingPage />);
    expect(baseElement).toBeTruthy();
  });
});
